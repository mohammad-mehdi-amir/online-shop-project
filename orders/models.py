from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
class order(models.Model):
    
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30,verbose_name=_('First Name :'))
    last_name=models.CharField(max_length=30,verbose_name=_('Last Name :'))
    phone_number= PhoneNumberField(null=False, blank=False)
    address=models.TextField(verbose_name=_('Address'))
    email=models.EmailField()
    
    datetime_order=models.DateField(auto_now_add=True)
    datetime_order_modified=models.DateField(auto_now=True)
    
    is_payed=models.BooleanField(default=False)
    
    order_note=models.TextField(blank=True,verbose_name=_('Do You Have Any Note For This Order?'))
    
    def __str__(self):
        return f'order: {self.id} -owner:{self.user}'
    
class order_item(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE,related_name='items')
    
    product=models.ForeignKey('products.product',on_delete=models.CASCADE)
    
    price=models.PositiveIntegerField()
    
    quantity=models.PositiveIntegerField(default=1)

    
    def __str__(self):
        return f'{self.product} fro order {self.order}'