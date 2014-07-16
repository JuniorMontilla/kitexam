from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('exam.apps.questions.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
)

error403  = 'questions.views.error403'
error404 = 'questions.views.error404'
error500 = 'questions.views.error500'
