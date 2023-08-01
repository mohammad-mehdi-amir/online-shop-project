from django import forms
from .models import blog

class new_blog_form(forms.ModelForm):
    class Meta:
        model = blog
        fields = ('title','text')
