from django.urls import path

from . import views

urlpatterns = [
	# example: /
	path('', views.index, name='index'),
]