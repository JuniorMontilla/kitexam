__author__ = 'Junior Montilla'
from django.conf.urls import patterns, url

urlpatterns = patterns('exam.apps.questions.views',
                       url(r'^$','index_view',name="url_index"),
                       url(r'^login/$','login_view',name='url_login'),	
                       url(r'^register/$','register_view',name='url_register'),	
                       url(r'^profile/$','profile_view',name='url_profile'),	
                       url(r'^python/$','python_view',name='url_python'),	
                       url(r'^gnu/$','gnu_view',name='url_gnu'),	
                       url(r'^logout/$','logout_view',name='url_logout'),	
                       )
