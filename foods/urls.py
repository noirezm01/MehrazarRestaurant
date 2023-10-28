# from django.contrib import admin
from django.urls import path
from . import views


app_name = 'foods'


urlpatterns = [
    path('', views.main, name='main'),
    path('foods/', views.food_list, name='food_list'),
    path('foods/<int:id>/', views.food_detail, name='food_detail'),
    # path('foods/blog', views.blog, name='blog'),
    path('foods/gallery', views.gallery, name='gallery'),

]
