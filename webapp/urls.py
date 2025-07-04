from django.urls import path
from .views import task_list, add_task, edit_task, delete_task, task_detail

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('<int:pk>/delete/', delete_task, name='delete_task'),
    path('<int:pk>/edit/', edit_task, name='edit_task'),
    path('<int:pk>/', task_detail, name='task_detail'),
]


