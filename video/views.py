from django.shortcuts import render
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm, NewVideoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        formA = 'Title'
        #return render(request, self.template_name, {'menu_active_item': 'home'})
        return render(request, self.template_name, {'formA': formA})



class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            print("already logged in. Redirecting")
            print(request.user)
            logout(request)
            return HttpResponseRedirect('/')
        formA = LoginForm()
        return render(request, self.template_name, {'formA': formA})

    def post(self, request):
        # Pass filled out HTML-Form from View to LoginForm()
        formA = LoginForm(request.POST)
        if formA.is_valid():
            username = formA.cleaned_data['username']
            password = formA.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('success login')
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('login')
        return HttpResponse("This is Login view. POST Request")



class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        if request.user.is_authenticated:
            print("already logged in. Redirecting")
            print(request.user)
            return HttpResponseRedirect('/')
        formA = RegisterForm()
        return render(request, self.template_name, {'formA': formA})

    def post(self, request):
        # Pass filled out HTML-Form from View to RegisterForm()
        formA = RegisterForm(request.POST)
        if formA.is_valid():
            # Create a User Account
            username = formA.cleaned_data['username']
            password = formA.cleaned_data['password']
            email = formA.cleaned_data['email']

            new_user = User(username = username, email = email)
            new_user.set_password(password)
            new_user.save()
            return HttpResponseRedirect('/login')
        return HttpResponse("This is Register view. POST Request")




class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        formA = NewVideoForm()
        return render(request, self.template_name, {'formA': formA})

    def post(self, request):
        return HttpResponse("This is Index view. POST Request")
