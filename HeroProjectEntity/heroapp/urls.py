from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero_list, name='hero_list'), # Read (list view)
    path('new/', views.hero_create, name='hero_create'), # Create
    path('<int:id>/edit/', views.hero_update, name='hero_update'), # Update
    path('<int:id>/delete/', views.hero_delete, name='hero_delete'), # Delete
]
