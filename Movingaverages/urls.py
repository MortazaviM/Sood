from django.conf.urls import url

from Movingaverages.views import MovingAveragesView, SupportView

#router = routers.DefaultRouter()
#router.register(r'get', DataViewSet, r"get")

urlpatterns=[
    #url(r'get/$', views.DataAPIView.as_view(), name='get'),
    url(r'(?P<pk>.+?)/detail/$', MovingAveragesView.as_view(), name='detail'),
    url(r'(?P<pk>.+?)/all/$', SupportView.as_view(), name='all'),
]

#[\w ]+
#[\w:|- ]+