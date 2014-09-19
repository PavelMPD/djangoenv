from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^view/$', 'notebook.views.view'),
)