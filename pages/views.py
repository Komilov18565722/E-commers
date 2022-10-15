from django.shortcuts import render, redirect
from products.models import Product
from django.contrib import messages
from django.db.models import Q
from products.views import delete_product
# Create your views here.

def home(request):    
    if  request.GET.get('text') :

        query_text = request.GET['text']

        context_1 = {
            "obj": Product.objects.filter(Q(title__contains=query_text) |
                                            Q(bio__contains=query_text) |
                                            Q(definition__contains=query_text) |
                                            Q(price__contains=query_text) |
                                            Q(count__contains=query_text) |
                                            Q(delivery_price__contains=query_text) |
                                            Q(users__username__contains=query_text) |
                                            Q(users__first_name__contains=query_text) |
                                            Q(users__last_name__contains=query_text)

                                            ),
        }
    else:
        context_1 = {
            "obj": Product.objects.order_by('-title')[:],
        }
    return render(request, template_name='home.html', context = context_1 )


def product(request, pk = None, card = None):
    if card and pk:
        user = request.user
        product_obj = Product.objects.filter(id = pk)[0]
        product_obj.users = user
        product_obj.save()

        obj = Product.objects.filter(id = pk)[0]
        if card == 1:          
            obj.card = 1
        elif card == 2:
            obj.card = 0
        obj.save()
        return render(request, template_name="product.html", context ={"obj" : obj} )
    elif pk:
        obj = Product.objects.filter(id = pk)[0]
        return render(request, template_name="product.html", context ={"obj" : obj} )

    else:
        return redirect('home')

def buy(request, pk = None):
    if request.user.is_authenticated:
        user = request.user
        product_obj = Product.objects.filter(id = pk)[0]
        product_obj.users = user
        product_obj.count = product_obj.count - 1
        product_obj.buy = 1
        if product_obj.count > 0 :
            product_obj.save()
        else:
            return delete_product(request, pk)
        return home(request)
    else:
        messages.warning(request, ("You must login before purchasing an item"))
        return redirect('/accounts/login/?next=%s' % request.path)

def checkout(request, pk = None):
    if pk:
        obj = Product.objects.filter(id = pk)[0]
        return render(request, template_name="checkout.html", context ={ "obj" : obj } )
    else:
        return redirect('home')

def user_purchases(request, card = None):
    
    if request.user.is_authenticated:
        if request.GET.get('text'):
            query_text = request.GET.get('text')
            obj = Product.objects.filter(users = request.user ).filter(
                                        Q(title__contains=query_text) |
                                        Q(definition__contains=query_text) |
                                        Q(price__contains=query_text) |
                                        Q(count__contains=query_text) |
                                        Q(delivery_price__contains=query_text) |
                                        Q(users__username__contains=query_text) |
                                        Q(users__first_name__contains=query_text) |
                                        Q(users__last_name__contains=query_text)
                                        )    
        else:
            if card:
                obj = Product.objects.filter(users = request.user ).filter(card = 1)
            else:
                obj = Product.objects.filter(users = request.user ).filter(buy = 1)
        return render(request, template_name="home.html", context ={ "obj" : obj } )
    else:
        messages.warning(request, ("You must login before purchasing an item"))
        return redirect('/accounts/login/?next=%s' % request.path)