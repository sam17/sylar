from django.conf.urls import patterns, include, url
from sylar.views import hello,home,compare
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', home),
	url(r'^compare/$',compare),
	#url(r'^thanyou$',thanks),
	#url(r'^results$',results),
    url(r'^hello/$', hello),
    
    # Examples:
    # url(r'^$', 'sylar.views.home', name='home'),
    # url(r'^sylar/', include('sylar.foo.urls')),


    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
