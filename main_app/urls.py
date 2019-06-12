from django.urls import path
from . import views
from django.urls import reverse

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('beasts/', views.beasts_index, name='index'),
    path('beasts/<int:beast_id>/', views.beasts_detail, name='detail'),
    path('beasts/create/', views.BeastCreate.as_view(), name='beasts_create'),
    path('beasts/<int:pk>/update/', views.BeastUpdate.as_view(), name='beasts_update'),
    path('beasts/<int:pk>/delete/', views.BeastDelete.as_view(), name='beasts_delete'),
    path('beasts/<int:beast_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    
]