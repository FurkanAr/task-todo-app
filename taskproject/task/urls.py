from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTaskForm, name="getTaskForm"),
    path('list', views.getTask, name="getTask"),
    path('update/<int:id>', views.updateTaskForm, name="updateForm"),
    path('delete/<int:id>', views.deleteTask, name="deleteTask"),

]
