from django import forms
from .models import NoteCategory
from django.contrib.auth.models import User

class NoteCategoryForm(forms.ModelForm):
    class Meta:
        model=NoteCategory
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control"})
        }

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username':forms.TextInput(attrs={'class':"form-control mt-2"}),
            'password':forms.PasswordInput(attrs={'class':"form-control mt-2"})
        }