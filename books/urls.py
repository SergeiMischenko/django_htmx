from django.urls import path

from .views import book_detail, book_list, create_book, update_book_details

urlpatterns = [
    path("", book_list, name="book_list"),
    path("create_book/", create_book, name="create_book"),
    path(
        "update_book_details/<int:pk>/", update_book_details, name="update_book_details"
    ),
    path("book_detail/<int:pk>/", book_detail, name="book_detail"),
]
