from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="prismal/index.html"), name="index"),
    # url(r'^$', 'prismal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^resume/', include('resume.urls', namespace="resume")),
    url(r'^admin/', include(admin.site.urls)),
)
