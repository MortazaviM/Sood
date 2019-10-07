from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import viewsets, generics
from Signal.models import data
from Signal.serializers import DataSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
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

class DataDetailView(APIView):
    #lookup_field = 'pk'
    def post(self, request, pk):
        mydata=get_object_or_404(data, pk=pk)
        Serialized_data=DataSerializer(mydata, many=True)
        return Response(Serialized_data.data)

    def get(self, request, pk):
        mydata=get_object_or_404(data, pk=pk)
        Serialized_data=DataSerializer(mydata, many=True)
        return Response(Serialized_data.data)





