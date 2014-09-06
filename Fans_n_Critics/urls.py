from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', include('webapp.urls')),
)
handler404 = 'webapp.views.failed'
handler500 = 'webapp.views.failed'
handler403 = 'webapp.views.failed'
handler400 = 'webapp.views.failed'
