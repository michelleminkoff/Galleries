from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'galleries/$', 'galleries.data.views.index'),
    (r'(?P<id>\d+)/$', 'galleries.data.views.detail'),
    (r'search_name', 'galleries.data.views.search_name'),
    (r'search_closed', 'galleries.data.views.search_closed'),
    (r'search_founded', 'galleries.data.views.search_founded'),
    (r'search_media', 'galleries.data.views.search_media'),
    (r'search_neighborhood', 'galleries.data.views.search_neighborhood'),
    (r'search_outcome', 'galleries.data.views.search_outcome'),
    (r'search_zipcode', 'galleries.data.views.search_zipcode'),


)