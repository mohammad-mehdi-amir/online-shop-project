from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('blog_list/',BlogListView.as_view(),name='blog_list'),
    path('<int:pk>/',BlogDetailView.as_view(),name='blog_detail'),
    path('edit/<int:pk>/,',BlogEditView.as_view(),name='blog_edit'),
    # path('blog_list/',NewBloglView.as_view(),name='new_blog'),
    

]
