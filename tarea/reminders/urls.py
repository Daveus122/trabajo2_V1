from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('update/<uuid:pk>/', views.update_reminder, name='update_reminder'),
    path('delete/<uuid:pk>/', views.delete_reminder, name='delete_reminder'),
]