from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import viewsets, generics
from Movingaverages.models import data
from Movingaverages.serializers import DataSerializer, MovingAverageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from Libclass.averages import Moving_Averages
from Libclass.cross import Cross


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from rest_framework.decorators import api_view
#@api_view(['POST', 'GET'])
#class DataAPIView(generics.RetrieveAPIView):
#    lookup_field = 'pk'
#    serializer_class = DataSerializer()
    #queryset=data.objects.values_list('OPEN')[:10]
#    def get_queryset(self):
#        return Response(data.objects.values_list('OPEN'))

#    def post(self,request):
#        d=data.objects.first()[:10]
#        r=DataSerializer(d, many=True)
#        return Response(r.data)
        #if r.is_valid():
            #return Response(data=r.data)
        #else:
            #return Response(d)









class MovingAveragesView(APIView, PageNumberPagination):
    #serializer_class = serializers.BrandSerializer
    pagination_class = CustomPagination
    #pagination_class=settings.DEFAULT_PAGINATION_CLASS
    #pagination_class = LimitOffsetPagination
    def post(self, request, pk):
        days_5=5
        days_8=8
        days_kol=90
        mydata=data.objects.values_list('CLOSE').filter(TICKER=pk)
        #ma55=Moving_Averages(mydata,55).moving_average()[-days_kol:]
        ma50=Moving_Averages(mydata,50).moving_average()[-days_kol:]
        #ma21=Moving_Averages(mydata,21).moving_average()[-days_kol:]
        ma20=Moving_Averages(mydata,20).moving_average()[-days_kol:]
        ma10=Moving_Averages(mydata,10).moving_average()[-days_kol:]
        #ma8=Moving_Averages(mydata,8).moving_average()[-days_kol:]
        ma5=Moving_Averages(mydata,5).moving_average()[-days_kol:]

        signal_5_values_ma1050=Cross(ma10[-days_5:], ma50[-days_5:]).up_points()
        signal_8_values_ma1050=Cross(ma10[-days_8:], ma50[-days_8:]).up_points()

        signal_5_values_ma520=Cross(ma5[-days_5:], ma20[-days_5:]).up_points()
        signal_8_values_ma520=Cross(ma5[-days_8:], ma20[-days_8:]).up_points()


        output={
            #'MA55':ma55,
            'moving_average_50':ma50,
            #'MA21':ma21,
            'moving_average_20': ma20,
            'moving_average_10':ma10,
            #'MA8':ma8,
            'ALEN_1050':{
                'desription':'قطع دو میانگین متحرک 10 روزه و 50 روزه با حاشیه ی 5 و 8 روزه',
                'signal_5':False if len(signal_5_values_ma1050)==0 else True,
                'signal_8':False if len(signal_8_values_ma1050)==0 else True,

            },
            'ALEN_520':{
                'desription':'قطع دو میانگین متحرک 5 روزه و 20 روزه با حاشیه ی 5 و 8 روزه',
                'signal_5':False if len(signal_5_values_ma520)==0 else True,
                'signal_8':False if len(signal_5_values_ma520)==0 else True,
            }
        }
        Serialized_data=MovingAverageSerializer(data=output)
        if Serialized_data.is_valid():
            return Response(Serialized_data.data)
        else:
            return Response({'Notworking'})



class SupportView(APIView):

    def post(self, request, pk):
        zdata={}
        mydata=data.objects.values_list('CLOSE').filter(TICKER=pk)
        paginator = Paginator(mydata, 100) 
        page = request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            post_list = paginator.page(1)
        except EmptyPage:
        # If page is out of range deliver last page of results
            post_list = paginator.page(paginator.num_pages)
        zdata={
                'number_of_pages':paginator.num_pages,
                'page': page,
                'post_list': list(post_list)
                   }
        return Response(data=zdata)
