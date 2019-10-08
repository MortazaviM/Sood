from django.conf.urls import url

from Movingaverages.views import MovingAveragesView

#router = routers.DefaultRouter()
#router.register(r'get', DataViewSet, r"get")

urlpatterns=[
    #url(r'get/$', views.DataAPIView.as_view(), name='get'),
    url(r'(?P<pk>.+?)/detail/$', MovingAveragesView.as_view(), name='detail'),
]

#[\w ]+
#[\w:|- ]+