from django.conf.urls import patterns, include, url
from django.contrib import admin
import backbone

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'first_django_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^basicview/', include('article.urls')),
    url(r'^articles/', include('article.urls')),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^mybackbone/', include('mybackbone.urls')),
    url(r'^notebook/', include('notebook.urls')),
    url(r'^filepicker/', include('filepicker.urls')),
    url(r'^myorders/', include('myorder.urls')),
)