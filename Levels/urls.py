from django.conf.urls import url
from Levels.views import ClosingDataView , SupportView

urlpatterns=[
    #url(r'get/$', views.DataAPIView.as_view(), name='get'),
    #url(r'(?P<pk>.+?)/detail/$', MovingAveragesView.as_view(), name='detail'),
    url(r'(?P<pk>.+?)/all/$', ClosingDataView.as_view(), name='data'),
    url(r'(?P<pk>.+?)/support/$', SupportView.as_view(), name='support'),

]
