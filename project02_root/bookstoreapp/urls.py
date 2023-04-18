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
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('pages/<int:page_id>/', views.page_view, name='page_detail'),

]

urlpatterns += staticfiles_urlpatterns()