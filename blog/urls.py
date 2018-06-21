from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'$^', views.paginaInicial),
	url(r'^sobre/', views.sobre),
	url(r'^contato/', views.contato),
	url(r'^games/', views.games)
]