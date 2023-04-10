from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.view_all_books, name='allbooks'),
    path('books/<int:id>', views.single_book, name='singlebook'),
    path('books/<str:book_category>', views.books_by_category, name='booksbycategory'),
]

urlpatterns += staticfiles_urlpatterns()