from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

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
