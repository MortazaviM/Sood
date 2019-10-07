from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import viewsets, generics
from Movingaverages.models import data
from Movingaverages.serializers import DataSerializer, MovingAverageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from Libclass.averages import Moving_Averages
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

class MovingAveragesView(APIView):
    def post(self, request, pk):
        mydata=data.objects.values_list('CLOSE').filter(TICKER=pk)
        ma55=Moving_Averages(mydata,55)
        ma50=Moving_Averages(mydata,50)
        ma21=Moving_Averages(mydata,21)
        ma20=Moving_Averages(mydata,20)
        ma10=Moving_Averages(mydata,10)
        ma8=Moving_Averages(mydata,8)
        output={
            'MA55':ma55,
            'MA50':ma50,
            'MA21':ma21,
            'MA20': ma20,
            'MA10':ma10,
            'MA8':ma8,
            'ALEN1050':{
                'desription':'',
                'signal5':'',
                'signal8':'',

            },
            'ALEN520':{
                'desription':'',
                'signal5':'',
                'signal8':'',
            }
        }
        Serialized_data=MovingAverageSerializer(output)
        return Response(Serialized_data.data)

    #def get(self, request, pk):
    #    mydata=get_object_or_404(data, pk=pk)
    #    Serialized_data=DataSerializer(mydata, many=True)
    #   return Response(Serialized_data.data)





