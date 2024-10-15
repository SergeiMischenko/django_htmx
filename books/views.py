from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from .forms import BookCreateForm
from .models import Book


@require_http_methods(["GET"])
def book_list(request):
    book_list = Book.objects.all()
    form = BookCreateForm(auto_id=False)
    return render(request, "base.html", {"book_list": book_list, "form": form})


@require_http_methods(["POST"])
def create_book(request):
    form = BookCreateForm(request.POST)
    if form.is_valid:
        book = form.save()
    return render(request, "partial_book_detail.html", {"book": book})
