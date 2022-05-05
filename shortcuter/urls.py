from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'home'),
    path('<slug:slug>', views.Short.as_view(), name = 'short'),
    path('add/', views.add_url, name = 'add'),
]
