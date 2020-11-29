from django import forms
from django.contrib.auth.models import User
class ContactForm(forms.Form):
	fullname = forms.CharField(
						widget=forms.TextInput(
							attrs={"class":"form-control",
							"placeholder":"your full name",
							}))

	email = forms.EmailField(widget =forms.EmailInput(attrs={"class":"form-control",
							"placeholder":"your email",
							}))

	description = forms.CharField(
						widget=forms.Textarea(
							attrs={"class":"form-control",
							"placeholder":"your Description",
							}))
	def clean_email(self):
		email = self.cleaned_data.get('email')
		if "google.com" not in email:
			raise forms.ValidationError("enter a valid email")
		return email

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput(
							attrs={ "class" : "form-control",
							}))

class RegisterForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField(widget =forms.EmailInput())
	password = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(label="confirm Password",widget=forms.PasswordInput())

	def clean_username(self):
		username =self.cleaned_data.get('username')
		qs = User.objects.filter(username = username)
		if qs.exists():
			raise forms.ValidationError("username is taken")
		else:
			return username

	def clean_email(self):
		email =self.cleaned_data.get('email')
		qs = User.objects.filter(email = email)
		if qs.exists():
			raise forms.ValidationError("email is taken")
		else:
			return email
	def clean(self):
		data =self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError("Passwords must match")
		else:
			return data
