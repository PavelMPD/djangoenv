from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^view/$', 'filepicker.views.view'),
    url(r'^test/$', 'filepicker.views.test'),
    url(r'^widget/$', 'filepicker.views.widget'),
)
