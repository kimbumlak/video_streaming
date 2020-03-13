from django import forms
from .models import *
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20)
    email = forms.CharField(label='Email', max_length=50)

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":80}))
    #text = forms.CharField(label='text', max_length=300)
    

# class NewVideoForm(forms.Form):
#     title = forms.CharField(label='Title', max_length=100)
#     description = forms.CharField(label='Description', max_length=300)
#     file = forms.FileField()


class NewVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        exclude = ['datetime', 'user']
    