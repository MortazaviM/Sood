from django.conf.urls import url

from Movingaverages.views import DataDetailView

#router = routers.DefaultRouter()
#router.register(r'get', DataViewSet, r"get")

urlpatterns=[
    #url(r'get/$', views.DataAPIView.as_view(), name='get'),
    url(r'(?P<pk>[\w:|-]+)/detail/$', views.DataDetailView.as_view(), name='detail'),
]