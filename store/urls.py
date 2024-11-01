from django.urls import path

from demo import admin
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<pk>/', views.product_details)
]
