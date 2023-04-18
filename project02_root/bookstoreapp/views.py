from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, get_connection
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Book, Page
from .contact import ContactForm
from .forms import CreateUserForm


def page_view(request, page_id):
    page = Page.objects.get(id=page_id)
    return render(request, 'page.html', {'page': page})

def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
          form = CreateUserForm(request.POST)
          if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account was created for " + user)

                return redirect("login")

    return render(request, 'register.html', {'form': form})


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Username or Password is incorrect")
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
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

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


