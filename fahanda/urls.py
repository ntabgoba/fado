from django.conf.urls import patterns, url
from fahanda import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^new/$', views.new, name='new'),
	url(r'^project/$', views.project, name='project'),
	url(r'^products/$', views.products, name='products'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),
)

