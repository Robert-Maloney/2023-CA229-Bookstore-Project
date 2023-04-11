from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.view_all_books, name='allbooks'),
    path('books/<int:id>', views.single_book, name='singlebook'),
    path('books/category/<str:book_category>', views.books_by_category, name='booksbycategory'),
    path('books/category', views.category, name='category'),
    path('contact/', views.contact, name='contact'),

]

urlpatterns += staticfiles_urlpatterns()