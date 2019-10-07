"""Sood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework_mongoengine import routers
from Signal import urls as SURL
from Signal.views import  DataDetailView
from Signal import views

#router = routers.DefaultRouter()
#router.register(r'signal', DataViewSet, r"signal")
#router.register(r'v1', views.ToolViewSet)
#router.register(r'v1/{id}/', views.ToolDetailViewSet.as_view(),'v1')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include(router.urls)),
    #url(r'^v1/(P<id>)}/$', views.ToolDetailViewSet.as_view(), name='search'),
    #url(r'^v1/create/$', views.ToolCreateViewSet.as_view(), name='create'),
    #url(r'^', views.DataDetailView.as_view(), name='a'),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
    #url(r'^api/signal/', include(SURL)),
]