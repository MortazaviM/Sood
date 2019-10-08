from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import viewsets, generics
from Movingaverages.models import data
from Movingaverages.serializers import DataSerializer, MovingAverageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from Libclass.averages import Moving_Averages
from Libclass.cross import Cross
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
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



class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })






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
            'MA50':ma50,
            #'MA21':ma21,
            'MA20': ma20,
            'MA10':ma10,
            #'MA8':ma8,
            'ALEN1050':{
                'desription':'قطع دو میانگین متحرک 10 روزه و 50 روزه با حاشیه ی 5 و 8 روزه',
                'signal5':False if len(signal_5_values_ma1050)==0 else True,
                'signal8':False if len(signal_8_values_ma1050)==0 else True,

            },
            'ALEN520':{
                'desription':'قطع دو میانگین متحرک 5 روزه و 20 روزه با حاشیه ی 5 و 8 روزه',
                'signal5':False if len(signal_5_values_ma520)==0 else True,
                'signal8':False if len(signal_5_values_ma520)==0 else True,
            }
        }
        Serialized_data=MovingAverageSerializer(data=output)
        if Serialized_data.is_valid():
            return Response(Serialized_data.data)
        else:
            return Response({'Notworking'})
