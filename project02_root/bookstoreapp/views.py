from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def view_all_books(request):
    allbooks = Book.objects.all()
    return render(request, 'all_books.html', {'allbooks': allbooks})

def single_book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'single_book.html', {'book': book})


def index(request):
    return render(request, 'index.html')
