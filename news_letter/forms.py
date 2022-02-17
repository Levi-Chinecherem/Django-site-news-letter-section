from django import forms
from .models import News_Letter

class News_Letter_Form(forms.ModelForm):
    class Meta:
        model = News_Letter
        fields = [
            'email'
        ]