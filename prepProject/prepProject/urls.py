from django.contrib import admin
from django.urls import path
from prepApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_login, name ="home_login"),
    path('play', views.play, name ="play"),
    path('play2', views.play2, name ="play2"),
    path('study/', views.study, name="study"),
    path('recordlist/', views.recordlist, name="recordlist"),
    path('checkcomplete/<int:pk>', views.checkcomplete, name ="checkcomplete"),
]