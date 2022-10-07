from django.urls import path
from .views import add_prodect

urlpatterns= [
    path('addproduct/', add_prodect, name = 'add_product'),
]