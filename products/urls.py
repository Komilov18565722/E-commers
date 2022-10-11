from django.urls import path
from .views import add_prodect, delete_product, update_product

urlpatterns= [
    path('addproduct/', add_prodect, name = 'add_product'),
    path('delete/<int:pk>', delete_product, name = 'delete'),
    path('update/<int:pk>', update_product, name = 'update'),

]