from django import forms
from .models import product

class new_product_form(forms.ModelForm):
    class Meta:
        model = product
        fields = ('title','des','price','image')

