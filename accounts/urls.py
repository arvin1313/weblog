from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile_view, name='profile_view'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
