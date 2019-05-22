from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # example: /
    path('', views.index, name='index'),
    # example: /login
    path('login', views.login, name='login'),
    # exapmle: /register
    path('register', views.register, name='register'),
    # example: /forum
    path('forum', views.forum_homepage, name='forum_homepage'),
    # example: /forum/upravuvanje-so-ikt-proekti
    path('forum/<slug:predmet>', views.forum_predmet, name='forum_predmet'),

    # API views
    # example: /api/login
    path('api/login', obtain_auth_token, name='api_login'),
    # example: /api/register
    path('api/register', views.api_register, name='api_register')
]
