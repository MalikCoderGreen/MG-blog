from django.urls import path
from ps_blog_app import views
from django.contrib import admin

app_name = 'ps_blog_app'
urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('upcoming_titles/', views.upcoming_titles, name='upcoming'),
    path('register/', views.register, name='register'),
    path('login_page/', views.login_page, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('categories/<category>/', views.blog_category, name='blog_category'),
]