from django.urls import path
from . import views


urlpatterns = [
     path('', views.index),
    path('login/', views.login_view),
    path('signup/',views.signup),
    path('home/',views.home),
    path('newpost/',views.newpost),
    path('mypost/',views.mypost),
    path('signout/',views.signout),

]