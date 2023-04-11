from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, get_connection

from .models import Book, Page
from .contact import ContactForm

def contact(request):
	submitted = False
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@dcu.ie'),
				['robert.maloney26@mail.dcu.ie'], 
				connection=con
			)
			return HttpResponseRedirect('/contact?submitted=True')
	else:
		form = ContactForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form': form,
		'page_list': Page.objects.all(),
		'submitted': submitted
	}
	return render(request, 'contact.html', context)


# Create your views here.
def view_all_books(request):
    allbooks = Book.objects.all()
    return render(request, 'all_books.html', {'allbooks': allbooks})

def single_book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'single_book.html', {'book': book})

def books_by_category(request, book_category):
    allbooks = Book.objects.filter(category=book_category)
    return render(request, 'all_books.html', {'allbooks': allbooks})

def category(request):
    category_set = set([x.category for x in Book.objects.all()])
    return render(request, 'category.html', {'categories': category_set})

def index(request):
    return render(request, 'index.html')
