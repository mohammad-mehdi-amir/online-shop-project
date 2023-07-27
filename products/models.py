from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=100)
    des=models.TextField()
    
    datetime_add=models.DateTimeField(auto_now_add=True)
    datetime_edit=models.DateTimeField(auto_now=True)
    
    price=models.PositiveIntegerField()
    status=models.BooleanField(default=True)
    
    image=models.ImageField(upload_to='product_img/')
    seller= models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_product', args=[self.id])
    
    
class comment(models.Model):
    text=models.TextField()
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE,related_name="comments")
    datetime_add=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text