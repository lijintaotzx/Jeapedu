from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Jeapedu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^course/$', 'Jeapedu.views.course', name='course'),
	url(r'^courseshow/(\d+)$', 'Jeapedu.views.courseshow', name='courseshow'),
	url(r'^teachers$', 'Jeapedu.views.teachers', name='teachers'),
	url(r'^$', 'Jeapedu.views.index', name='index'),
	
    url(r'^media(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT,'show_indexes':True}),
	
)
