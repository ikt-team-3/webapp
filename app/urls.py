from django.urls import path

from . import views

urlpatterns = [
    # example: /
    path('', views.index, name='index'),

    # example: /login
    path('login', views.login, name='login'),

    # exapmle: /register
    path('register', views.register, name='register'),
]
