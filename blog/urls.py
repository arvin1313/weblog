from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:slug>/', views.article_detail, name='article_detail'),
    path('articles/', views.article_list, name='article_list'),
    path('search/', views.search, name='article_search'),
    path('tag/<int:tag_id>/', views.article_tag, name='article_tag'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]