from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.forms,name='forms'),
    path('add_item',views.add_item,name='add_item'),
    path('get_items',views.get_items,name='get_items'),
    path('edit_item',views.edit_item,name='edit_item'),
    path('update_item',views.update_item,name='update_item'),
    path('delete_item',views.delete_item,name='delete_item')


]