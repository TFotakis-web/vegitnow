from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.translation import gettext
from django.views.generic import View

from .forms import RegisterForm


class LoginFormView(View):
	form_class = AuthenticationForm
	template_name = 'login/login.html'

	def get(self, request):
		if request.user.is_authenticated:
			return redirect('general:home')
		form = self.form_class(None)
		context = {
			'title': gettext('Login') + ' - VegItNow',
			'form': form
		}
		return render(request, self.template_name, context=context)

	def post(self, request):
		form = self.form_class(data=request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('general:home')
		context = {
			'title': gettext('Login') + ' - VegItNow',
			'form': form
		}
		return render(request, self.template_name, context=context)


class RegisterFormView(View):
	form_class = RegisterForm
	template_name = 'login/register.html'

	def get(self, request):
		form = self.form_class(None)
		context = {
			'title': gettext('Register') + ' - VegItNow',
			'form': form
		}
		return render(request, self.template_name, context=context)

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('general:home')
		context = {
			'title': gettext('Register') + ' - VegItNow',
			'form': form
		}
		return render(request, self.template_name, context=context)


def logoutView(request):
	logout(request)
	return redirect('login:login')
