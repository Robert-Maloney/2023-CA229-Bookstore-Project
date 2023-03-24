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

def books_by_year(request, book_year):
    allbooks = Book.objects.filter(year=book_year)
    return render(request, 'all_books.html', {'allbooks': allbooks})

def books_by_category(request, book_category):
    allbooks = Book.objects.filter(category=book_category)
    return render(request, 'all_books.html', {'allbooks': allbooks})

def category(request):
    category_set = set([x.category for x in Book.objects.all()])
    return render(request, 'category.html', {'categories': category_set})

def year(request):
    year_set = set([x.year for x in Book.objects.all()])
    return render(request, 'year.html', {'years': year_set})

def books_by_year_and_category(request, book_category, book_year):
    print(book_category, book_year)
    allbooks = Book.objects.filter(category=book_category, year=book_year)
    return render(request, 'all_books.html', {'allbooks': allbooks})

def yearcategory(request):
    year_category_set = set([(x.category, x.year) for x in Book.objects.all()])
    return render(request, 'yearandcategory.html', {'yearcategories': year_category_set})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        year = request.POST['year']
        price = request.POST['price']
        synopsis = request.POST['synopsis']
        category = request.POST['category']
        book = Book(title=title, author=author, year=year, price=price, synopsis=synopsis, category=category)
        book.save()
        return render(request, 'add_book.html')
    else:
        return render(request, 'add_book.html')

def delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return HttpResponseRedirect(reverse('allbooks'))

def index(request):
    return render(request, 'index.html')
