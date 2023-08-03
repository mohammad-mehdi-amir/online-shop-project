from django.db import models
from django.contrib.auth import get_user_model
# from django.shortcuts import get_absolute_url
from django.urls import reverse_lazy
from ckeditor.fields import RichTextField
# Create your models here.

class blog(models.Model):
    title=models.CharField(max_length=100)
    text=RichTextField()
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    datetime_add=models.DateTimeField(auto_now_add=True)
    datetime_edit=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse_lazy('blog_detail',args=[ self.id])