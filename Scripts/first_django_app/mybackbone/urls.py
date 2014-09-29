from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'bbevents/$', 'mybackbone.views.bbevents'),
    url(r'bbmodel/$', 'mybackbone.views.bbmodel'),
    url(r'utemplate/$', 'mybackbone.views.utemplate'),
    url(r'bbview/$', 'mybackbone.views.bbview'),
    url(r'bbcollection/$', 'mybackbone.views.bbcollection'),
    url(r'bbcollection2/$', 'mybackbone.views.bbcollection2'),
)
