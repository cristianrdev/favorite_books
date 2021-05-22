from django.forms import  Textarea
from django import forms
from ..models import Book
# from django.forms import widgets


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = {'title', 'description'}

        widgets = {
            'title' : forms.TextInput(attrs = {'class':'form-control '}),
            'description': Textarea(attrs = {'class':'form-control ', 'rows':"2", 'style':'resize: none;'}),
        }



        labels = {
            'title' : "Titulo del libro",
            'description' : "Descripción"
        }


