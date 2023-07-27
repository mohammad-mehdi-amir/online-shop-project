from django import forms
from .models import product,comment

class new_product_form(forms.ModelForm):
    class Meta:
        model = product
        fields = ('title','des','price','image')

class commentForm(forms.ModelForm):
    class Meta:
        model=comment
        fields=('text',)