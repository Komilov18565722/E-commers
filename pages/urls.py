from django.urls import path
from .views import home, product
urlpatterns = [
    path('', home, name = 'home'),
    path('product/<int:pk>/', product , name = 'product'),
]