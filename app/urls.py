from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # example: /
    path('', views.index, name='index'),
    # example: /login
    path('login', views.login, name='login'),
    # example: /logout
    path('logout', views.logout, name='logout'),
    # exapmle: /register
    path('register', views.register, name='register'),
    # example: /forum
    path('forum', views.forum_homepage, name='forum_homepage'),
    # example: /forum/upravuvanje-so-ikt-proekti
    path('forum/<slug:predmet>', views.forum_predmet, name='forum_predmet'),
    # example: /forum/upravuvanje-so-ikt-proekti/1
    path('forum/<slug:predmet>/<int:tema>', views.forum_tema, name='forum_tema'),
    # example: /forum/upravuvanje-so-ikt-proekti/new
    path('forum/<slug:predmet>/new', views.forum_nova_tema, name='forum_nova_tema'),
    # example: /raspored
    path('raspored', views.raspored_prikaz, name='raspored_prikaz'),
    # example: /raspored/izbor
    path('raspored/izbor', views.raspored_izbor, name='raspored_izbor'),

    # API views
    # example: /api/login
    path('api/login', obtain_auth_token, name='api_login'),
    # example: /api/register
    path('api/register', views.api_register, name='api_register'),
    # example: /api/forum
    path('api/forum', views.api_forum_homepage, name='api_forum_homepage'),
    # example: /api/forum/upravuvanje-so-ikt-proekti
    path('api/forum/<slug:predmet>', views.api_forum_predmet, name='api_forum_predmet'),
    # example: /api/forum/upravuvanje-so-ikt-proekti/1
    path('api/forum/<slug:predmet>/<int:tema>', views.api_forum_tema, name='api_forum_tema'),
    # example: /api/forum/upravuvanje-so-ikt-proekti/new
    path('api/forum/<slug:predmet>/new', views.api_forum_nova_tema, name='api_forum_nova_tema'),
    # example: /api/profesori
    path('api/profesori', views.api_profesori, name='api_profesori'),
    # example: /api/raspored
    path('api/raspored', views.api_raspored_prikaz, name='api_raspored_prikaz'),
    # example: /api/raspored/izbor
    path('api/raspored/izbor', views.api_raspored_izbor, name='api_raspored_izbor'),
]
