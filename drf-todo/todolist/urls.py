from django.urls import path

from todolist.views import ListTodo, DetailTodo

urlpatterns = [
    path("", ListTodo.as_view()),
    path("<int:pk>/", DetailTodo.as_view()),
]
