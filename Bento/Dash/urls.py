from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_widget, name='add_widget'),
    path('delete/<int:widget_id>/', views.delete_widget, name='delete_widget'),
]