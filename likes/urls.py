from django.contrib import admin
from django.urls import path, include
from.views import add_like,remove_like,LikeListView
urlpatterns = [
    path('add/<int:pk>',add_like,name='add_like'),
    path('remove/<int:pk>',remove_like,name='remove_like'),
    path('list/',LikeListView.as_view(),name='list_like'),
    

]