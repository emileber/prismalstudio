from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from solid_i18n.urls import solid_i18n_patterns
#from django.utils.translation import ugettext_lazy as _

from django.contrib import admin
admin.autodiscover()


# urlpatterns = [
#     url(r'^sitemap\.xml$', 'sitemap.view', name='sitemap_xml'),
# ]

urlpatterns = patterns('',
    
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # url(r'^$', 'prismal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',content_type='text/plain')),
)

urlpatterns += solid_i18n_patterns('',
    url(r'^$', TemplateView.as_view(template_name="prismal/index.html"), name="index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^resume/', include('resume.urls', namespace="resume")),
    #url(r'^blog/', include('resume.urls', namespace="resume")),
)
