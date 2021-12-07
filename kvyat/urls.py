from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'kvyat'
urlpatterns = [
    path('', views.create, name='create'),
    path('<int:room_id>/', views.room, name='room'),
    path('<int:room_id>/join', views.join, name='join'),
    path('<int:room_id>/temp/guest', views.temp_guest, name='temp_guest'),
    path('login/', auth_views.LoginView.as_view(template_name='kvyat/login.html'), name="login"),
    path('register/', views.register_view, name='register'),
    path('<int:user_id>/profile', views.profile, name='profile'),
    path('top/', views.top, name='top'),
    path('about/', views.about, name='about'),
    path('creator/', views.creator, name='creator'),
    path('contact/', views.contact, name='contact'),
    path('create_room/', views.create_room, name='create_room'),
    path('<int:room_id>/remove_room/', views.remove_room, name='remove_room'),
    path('create_user/', views.create_user, name='create_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('<int:user_id>/logout_user/', views.logout_user, name='logout_user'),
]