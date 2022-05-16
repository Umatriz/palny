from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'home'),
    path('p/', views.links_list, name = 'profile'),
    path('p/<int:pk>/<slug:slug>', views.short, name = 'short'),
    path('add/', views.add_url, name = 'add'),
    path('edit/<int:pk>/', views.update_link, name = 'edit'),
    path('delete/<int:pk>/', views.delete_link, name = 'delete'),
]
