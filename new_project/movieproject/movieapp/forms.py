from .models import movie
from django import forms
class MovieForm(forms.ModelForm):
    class Meta:
        model=movie
        fields=['name','desc','year','img']
