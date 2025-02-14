from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_pessoa, name='add_pessoa'),
    path('delete/<int:pk>/', views.delete_pessoa, name='delete_pessoa'),
]