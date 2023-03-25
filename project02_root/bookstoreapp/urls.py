from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.view_all_books, name='allbooks'),
    path('books/<int:id>', views.single_book, name='singlebook'),

]

urlpatterns += staticfiles_urlpatterns()