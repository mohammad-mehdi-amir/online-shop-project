from django import forms
from .models import order


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ('first_name','last_name','phone_number','address','order_note','email')
