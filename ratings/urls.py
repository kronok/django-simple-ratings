from django.urls import re_path


urlpatterns = ['ratings.views',
    re_path(r'^rate/(?P<ct>\d+)/(?P<pk>[^\/]+)/(?P<score>\-?[\d\.]+)/$', 'rate_object', name='ratings_rate_object'),
    re_path(r'^unrate/(?P<ct>\d+)/(?P<pk>[^\/]+)/$', 'rate_object', {'add': False}, name='ratings_unrate_object'),
]
