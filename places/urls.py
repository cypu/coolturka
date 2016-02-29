from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'places.views.view_map')

)
