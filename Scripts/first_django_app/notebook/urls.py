import backbone

from django.conf.urls import patterns, url, include

backbone.autodiscover()

urlpatterns = patterns('',
    url(r'^view/$', 'notebook.views.view'),
    url(r'^save/$', 'notebook.views.save'),
    url(r'^load/$', 'notebook.views.load'),
    url(r'^backbone/', include(backbone.site.urls)),
)