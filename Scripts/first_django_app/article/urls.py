from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'first_django_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^1/', 'article.views.basic_one'),
    url(r'^2/', 'article.views.first_view'),
    url(r'^3/', 'article.views.second_view'),
    url(r'^all/$', 'article.views.articles'),
    url(r'^get/(?P<id>\d+)/$', 'article.views.article'),
    url(r'^addlike/(?P<id>\d+)/$', 'article.views.addlike'),
    url(r'^addcomment/(?P<id>\d+)/$', 'article.views.addcomment'),
)
