from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^simpleone/$', 'notebook.views.simpleone'),
    url(r'^view/$', 'notebook.views.view'),
    url(r'^edit/$', 'notebook.views.edit'),
)
