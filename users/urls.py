from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='manage'),
	url(r'^criar/$', views.create, name='create'),
	url(r'^editar/$', views.create, name='update'),
	url(r'^dados/$', views.view, name='view'),
]