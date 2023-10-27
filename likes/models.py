from django.db import models
from django.contrib.auth import get_user_model
from products.models import product

class like(models.Model):
    user=models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE,)
    
    def __str__(self):
        return f'{ self.product}'
    
    
    