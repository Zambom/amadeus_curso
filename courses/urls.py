from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^cursos/$', views.IndexView.as_view(), name='manage'),
	url(r'^cursos/criar/$', views.create, name='create'),
	url(r'^cursos/editar/([\w_-]+)/$', views.update, name='update'),
	url(r'^cursos/([\w_-]+)/$', views.view, name='view'),
	url(r'^cursos/categoria/([\w_-]+)/$', views.filter_cat, name='filter'),
	url(r'^categorias/$', views.index_cat, name='manage_cat'),
	url(r'^categorias/criar/$', views.create_cat, name="create_cat"),
	url(r'^categorias/editar/([\w_-]+)/$', views.update_cat, name='update_cat'),
	url(r'^categorias/([\w_-]+)/$', views.view_cat, name='view_cat'),
	url(r'^curso/([\w_-]+)/modulos/$', views.index_modules, name='manage_mods'),
	url(r'^curso/([\w_-]+)/modulos/cirar/$', views.create_modules, name='create_mods'),
	url(r'^curso/([\w_-]+)/modulos/editar/([\w_-]+)/$', views.update_modules, name='update_mods'),
]