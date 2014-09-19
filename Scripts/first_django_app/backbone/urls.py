from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'bbevents/$', 'backbone.views.bbevents'),
    url(r'bbmodel/$', 'backbone.views.bbmodel'),
    url(r'utemplate/$', 'backbone.views.utemplate'),
    url(r'bbview/$', 'backbone.views.bbview'),
    url(r'bbcollection/$', 'backbone.views.bbcollection'),
    url(r'bbcollection2/$', 'backbone.views.bbcollection2'),
)
