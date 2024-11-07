from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Landing page as the root URL
    path('heroes/', views.hero_list, name='hero_list'),  # URL for listing heroes
    path('hero/create/', views.hero_create, name='hero_create'),
    path('hero/update/<int:id>/', views.hero_update, name='hero_update'),
    path('hero/delete/<int:id>/', views.hero_delete, name='hero_delete'),
]
