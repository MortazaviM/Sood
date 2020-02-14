from django.shortcuts import render, HttpResponse
from Sood.models import data, indexstock
import datetime
from dateutil.relativedelta import relativedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from Movingaverages.views import calculateMA
import pandas as pd
import json
from operator import itemgetter
from Libclass.lines import HorizontalLines

def index(request):
    AllData={}
    To, Ha, Fi, Fa=[],[],[],[]
    Date=[]


    index_total = indexstock.objects.order_by("-DTYYYYMMDD").get_data("شاخص_كل6")
    index_hamvazn = indexstock.objects.order_by("-DTYYYYMMDD").get_data("شاخص_كل_(هم_وزن)6")
    index_fifty = indexstock.objects.order_by("-DTYYYYMMDD").get_data("شاخص_قيمت_50_شركت6")
    index_fara = indexstock.objects.order_by("-DTYYYYMMDD").get_data("شاخص_كل_فرابورس6")
    
#_CommandCursor__data
    for total,hamvazn,fifty,fara in zip(index_total,index_hamvazn,index_fifty,index_fara): 
        Date.append(total["DTYYYYMMDD"])
        To.insert(0,total["CLOSE"])
        Ha.insert(0,hamvazn["CLOSE"])
        Fi.insert(0,fifty["CLOSE"])
        Fa.insert(0,fara["CLOSE"])

    today=str(Date[0])[0:4] +'-'+str(Date[0])[4:6] +"-"+ str(Date[0])[6:8]
    
    end_date = datetime.datetime.strptime(today, '%Y-%m-%d')
    start_date = end_date.date() - relativedelta(months=+1)

    #vol_top=data.objects.order_by('-VOL').get_range("DTYYYYMMDD",str(end_date.year)+str(end_date.month)+str(end_date.day), str(start_date.year)+str(start_date.month)+str(start_date.day))

    #AllData['Vol']=vol_top
    AllData['Today']=today
    AllData['Date']=Date
    AllData['Total']=To
    AllData['Hamvazn']=Ha
    AllData['Fifty']=Fi
    AllData['Fara']=Fa

    return render(request, 'index.html',{'data':AllData})


def stock(request, pk):
    t1=datetime.datetime.now()
    if request.method == "GET":
        if ('pk' != ""):
            result=stockDataGenerator(pk)
            return render(request,'stock.html',{'data':result})



def stockDataGenerator(pk):
    days_limit=55
    values=data.objects.order_by("-DTYYYYMMDD").get_by_mil(pk)
    dd=list(values)
    close_data=[item['close'] for item in dd]
    support_point,min_list_dicts=HorizontalLines(close_data, days_limit).find_Support_point()
    resistance_point,max_list_dicts=HorizontalLines(close_data, days_limit).find_Resistance_point()
    #getter = itemgetter('Date','OPEN','HIGH', 'LOW','CLOSE')
    #zz=[list(getter(item)) for item in dd]
    if values:
        ma50,ma20,ma10,ma5=calculateMA(pk,264)
        result={
            'title':str(pk),
            'ma50':ma50,
            'ma20':ma20,
            'ma10':ma10,
            'ma5':ma5,
            'data':dd,
            'level':min_list_dicts+max_list_dicts,
            }
        return result





class SearchView(APIView):
    def get(self,request):
        pass

    def post(self, request):
        mapping = {
            'ک':'ك',
            'د':'دِ',
            'ب':'بِ',
            'ز':'زِ',
            'ذ':'ذِ',
            'ش':'شِ',
            'س':'سِ',
            'ی':'ى',
            'ی':'ي'
            }
        q = request.data.get('search', '')
        q=q.replace('ی',mapping['ی']).replace('ک',mapping['ک'])
        if len(q)>2:
            names=data.objects.values_list('TICKER').filter(TICKER__icontains=q).distinct('TICKER')
            company =data.objects.values_list('COMPANY').filter(TICKER__icontains=q).distinct('COMPANY')
            
            result={
                'names':names,
                'company':company
            }
        return Response(data=result)



class StockData(APIView):
    def get(self,request):
        q = request.GET.get('name', '')
        result=stockDataGenerator(q)
        return Response(data=result)

    def post(self, request):
        q = request.POST.get('name', '')
        result=stockDataGenerator(q)
        return Response(data=result)