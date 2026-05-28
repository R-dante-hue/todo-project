from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list_view, name='task_list'),
    path('task/<int:pk>/', views.task_detail_view, name='task_detail'),
    path('create/', views.task_create_view, name='task_create'),
    path('<int:pk>/delete/', views.task_delete_view, name='task_delete'),
]