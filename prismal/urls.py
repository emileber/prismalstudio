from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prismal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^resume/', include('resume.urls', namespace="resume")),
    url(r'^admin/', include(admin.site.urls)),
)
