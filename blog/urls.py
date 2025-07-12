from django.urls import path
from . import views


urlpatterns = [
     path('', views.index),
    path('login/', views.login_view),
    path('signup/',views.signup),
    path('home/', views.home, name='home'),
    path('newpost/',views.newpost),
    path('mypost/',views.mypost),
    path('signout/',views.signout),
    path('update/<int:blog_id>/', views.update_blog, name='update_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),

]