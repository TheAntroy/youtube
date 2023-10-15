from django.urls import path

from books import views

app_name = "books"
urlpatterns = [
    path("", views.list_books, name="list_books"),
    path("delete/<uuid:book_id>/", views.delete_book, name="delete_book"),
    path("book_form/", views.display_book_form, name="book_form"),
]
