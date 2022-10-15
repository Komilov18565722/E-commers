from django.urls import path
from .views import buy, checkout, home, product, user_purchases
urlpatterns = [
    path('', home, name = 'home'),
    path('search/', home),
    path('product/<int:pk>/<int:card>/', product , name = 'product'),
    path('product/<int:pk>/', product , name = 'product'),
    path('checkout/<int:pk>/', checkout, name = 'checkout'),
    path('buy/<int:pk>/', buy, name = 'buy'),
    path('user_purchases/<int:card>/', user_purchases, name = 'user_purchases'),
    path('user_purchases/', user_purchases, name = 'user_purchases'),
    path('user_purchases/search/', user_purchases),

]