from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'locations.views.view_map')

)