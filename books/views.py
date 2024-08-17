from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
# Create your views here.
