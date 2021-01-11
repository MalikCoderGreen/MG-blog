from django.urls import path
from ps_blog_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('upcoming_titles/', views.upcoming_titles, name='upcoming'),
    path('login_page', views.login_page, name='login'),
]