from operator import mod
from pyexpat import model
from turtle import mode
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.

class category(models.Model):
    image = models.ImageField(upload_to="category_img/",blank=True)
    title= models.CharField(max_length=50)
    descriptions= RichTextField()
    
    def __str__(self) -> str:
        return self.title


class product(models.Model):
    
    
    title = models.CharField(max_length=100)
    des = RichTextField()

    category_product=models.ForeignKey(category,on_delete=models.PROTECT,blank=True,null=True,related_name='product')
    
    datetime_add = models.DateTimeField(auto_now_add=True)
    datetime_edit = models.DateTimeField(auto_now=True)

    price = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    inventory=models.IntegerField(default=10)

    image = models.ImageField(upload_to="product_img/")
    seller = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_product", args=[self.id])

    objects = models.Manager()


class Active_comment(models.Manager):
    def get_queryset(self):
        return super(Active_comment, self).get_queryset().filter(active=True)


class comment(models.Model):
    option = [
        ("1", _("very bad")),
        ("2", _("bad")),
        ("3", _("normal")),
        ("4", _("good")),
        ("5", _("very good")),
    ]
    text = models.TextField(verbose_name=_("write your comment"))
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="comments"
    )
    product = models.ForeignKey(
        product, on_delete=models.CASCADE, related_name="comments"
    )
    datetime_add = models.DateTimeField(auto_now_add=True)
    rate = models.CharField(
        max_length=10, choices=option, blank=True, verbose_name=_("rate this product")
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):

        return reverse("detail_product", args=[self.product.id])

    object = models.Manager()
    active_comment_manager = Active_comment()
