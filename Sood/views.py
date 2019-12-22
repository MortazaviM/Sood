from django.shortcuts import render, HttpResponse
from Sood.models import data

def index(request):
    AllData={}
    To, Ha, Fi, Fa=[],[],[],[]

    index_total = data.objects.order_by("-DTYYYYMMDD").get_data("شاخص_كل6")
    index_hamvazn = data.objects.order_by("-DTYYYYMMDD").get_data("شاخص_كل_(هم_وزن)6")
    index_fifty = data.objects.order_by("-DTYYYYMMDD").get_data("شاخص_قيمت_50_شركت6")
    index_fara = data.objects.order_by("-DTYYYYMMDD").get_data("شاخص_كل_فرابورس6")
    
    for total,hamvazn,fifty,fara in zip(index_total,index_hamvazn,index_fifty,index_fara): 
        To.insert(0,total["CLOSE"])
        Ha.insert(0,hamvazn["CLOSE"])
        Fi.insert(0,fifty["CLOSE"])
        Fa.insert(0,fara["CLOSE"])

    AllData['Total']=To
    AllData['Hamvazn']=Ha
    AllData['Fifty']=Fi
    AllData['Fara']=Fa

    return render(request, 'index.html',{'data':AllData})