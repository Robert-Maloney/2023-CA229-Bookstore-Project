from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.view_all_books, name='allbooks'),
    path('books/<int:id>', views.single_book, name='singlebook'),
    path('books/year/<int:book_year>', views.books_by_year, name='booksbyyear'),
    path('books/category/<str:book_category>', views.books_by_category, name='booksbycategory'),
    path('books/category', views.category, name='category'),
    path('books/year', views.year, name='year'),
    path('books/category/<str:book_category>/year/<int:book_year>', views.books_by_year_and_category, name='bookysbyyearandcategory'),
    path('books/categoryandyear', views.yearcategory, name='yearcategory'),
    path('books/add', views.add_book, name='addbook'),
    path('delete/<int:id>', views.delete, name='delete'),
]
