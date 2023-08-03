"""cofig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
 
urlpatterns = [
    path('',views.home_view,name='home'),
    path('list_product/',views.ProductListView.as_view(),name='list_prodcut'),
    path('new_product/',views.NewProductView.as_view(),name='new_prodcut'),
    path('<int:pk>/',views.ProductDetailView.as_view(),name='detail_product'),
    path('comment/<int:pk>/',views.CommentCreateView.as_view(),name='new_comment'),

]
