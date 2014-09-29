from django.conf.urls import patterns, url, include
import backbone

backbone.autodiscover()

urlpatterns = patterns('',
    url(r'list/$', 'myorder.views.list'),
    url(r'^backbone/', include(backbone.site.urls)),
)
