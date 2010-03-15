from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('galleries.data.views',
    (r'galleries/$', 'index'),
    (r'(?P<id>\d+)/$', 'detail'),
    (r'search_name', 'search_name'),
    (r'search_closed', 'search_closed'),
    (r'search_founded', 'search_founded'),
    (r'search_media', 'search_media'),
    (r'search_neighborhood', 'search_neighborhood'),
    (r'search_outcome', 'search_outcome'),
    (r'search_zipcode', 'search_zipcode'),


)