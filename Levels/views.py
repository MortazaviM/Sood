from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.views import APIView
from rest_framework.response import Response
from Levels.models import data
from Libclass.lines import HorizontalLines
# Create your views here.

class ClosingDataView(APIView):
    def post(self, request, pk):
        zdata={}
        close_data=data.objects.values_list('CLOSE').filter(TICKER=pk)
        paginator = Paginator(close_data, 100) 
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

class OpeningDataView(APIView):
    def post(self, request, pk):
        zdata={}
        open_data=data.objects.values_list('OPEN').filter(TICKER=pk)
        paginator = Paginator(open_data, 100) 
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


class SupportView(APIView):
    def post(self, request, pk, day):
        days_limit=day
        close_data=data.objects.values_list('CLOSE').filter(TICKER=pk)
        support_point=HorizontalLines(close_data, days_limit).find_Support_point()
        zdata={
            'support_points': support_point,
        }
        return Response(data=zdata)

class ResistanceView(APIView):
    def post(self, request, pk, day):
        days_limit=day
        close_data=data.objects.values_list('CLOSE').filter(TICKER=pk)
        resistant_point=HorizontalLines(close_data, days_limit).find_Resistance_point()
        zdata={
            'resistant_points': resistant_point,
        }
        return Response(data=zdata)
