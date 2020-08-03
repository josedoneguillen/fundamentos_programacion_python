from django.shortcuts import render
from django.views.generic import ListView

from .models import Book

# Create your views here.
class BooksList(ListView):
    model = Book
    template_name = "core/books_list.html"