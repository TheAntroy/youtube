from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.index),
    path('insert_item', views.insert_item, name='insert_item'),
    path('delete_item/<int:todo_id>/', views.delete_item, name='delete_item'),
]
