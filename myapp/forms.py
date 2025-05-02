from django import forms
from .models import NoteCategory

class NoteCategoryForm(forms.ModelForm):
    class Meta:
        model=NoteCategory
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control"})
        }

class UserRegisterForm(forms.ModelForm):
    pass