from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import ContactForm , LoginForm ,RegisterForm

def home_page(request):
	context = {"title" : "Welcome Home Page!",
				"content": "this is your Home Page"}
	if request.user.is_authenticated:
		context['premium_content']='user authenticated'
	return render(request,"Contact/home.html",context=context)

def index(request):
	contact_form = ContactForm(request.POST or None)
	content = {"title" : "welcome Page" ,
				"content": "Hello To Welcom PAGE !",
				"form":contact_form }
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method == "POST":
	# 	print(request.POST)
	# 	print(request.POST.get('full-name'))
	return render(request,"Contact/index.html",context= content)

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		'form':form
	}
	print("User is Logged in")
	print(request.user.is_authenticated)
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request,username=username,password =password)
		print(request.user.is_authenticated)
		if user is not None:
			login(request, user)
			#context['forms'] = LoginForm()
			return redirect("/")
		else:
			print(request.user.is_authenticated,"not auth")
			print("Error")
	
	return render(request,"auth/login.html",context=context)

def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		'form':form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		user = User.objects.create_user(username,email,password)
		print(user)
	return render(request,"auth/register.html",context=context)