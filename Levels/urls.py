from django.conf.urls import url
from Levels.views import ClosingDataView , SupportView

urlpatterns=[
    #url(r'get/$', views.DataAPIView.as_view(), name='get'),
    #url(r'(?P<pk>.+?)/detail/$', MovingAveragesView.as_view(), name='detail'),
    url(r'all/(?P<pk>.+?)/$', ClosingDataView.as_view(), name='data'),
    url(r'support/(?P<pk>.+?)/(?P<day>\d{1,2})/$', SupportView.as_view(), name='support'),

]
