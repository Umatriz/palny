from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'home'),
    path('p/', views.links_list, name = 'profile'),
    path('p/<int:pk>/<slug:slug>', views.Short.as_view(), name = 'short'),
    path('add/', views.add_url, name = 'add'),
]
