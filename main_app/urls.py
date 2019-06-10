from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('beasts/', views.beasts_index, name='index'),
    path('beasts/<int:beast_id>/', views.beasts_detail, name='detail'),
]