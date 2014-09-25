from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^view/$', 'notebook.views.view'),
    url(r'^save/$', 'notebook.views.save'),
    url(r'^load/$', 'notebook.views.load'),
)