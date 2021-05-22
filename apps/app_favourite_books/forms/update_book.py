from apps.app_login_register.models import User
from django.forms import ModelForm, Textarea
from django import forms
from ..models import Book
from django.forms import widgets

class UpdateBookForm(ModelForm):
    # uploaded_by = ModelChoiceField(queryset=User.objects(id = 4))
    # error_css_class = 'error'
    # required_css_class = 'required'
    # title=forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    # description=forms.CharField(widget=forms.PasswordInput(), label='Confirme su contraseña')
    class Meta:
        model = Book
        fields = ['title', 'description']
        
        widgets = {
      
            'description': Textarea(attrs = {'class':'form-control ', 'rows':"2", 'style':'resize: none;'}),
        }


      