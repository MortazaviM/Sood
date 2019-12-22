from django.shortcuts import render, HttpResponse
from Sood.models import data

def index(request):
    index_all = data.objects.order_by("-DTYYYYMMDD").get_data("شاخص_كل6")
    a=[]
    for post in index_all: 
        a.insert(0,post["CLOSE"])
    return render(request, 'index.html',{'data':a})