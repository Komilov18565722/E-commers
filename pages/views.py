from django.shortcuts import render, redirect
from accounts.models import CustomUser
from products.models import Product

# Create your views here.

def home(request):
    print(0000000000000000000000000000000,type(Product.objects.order_by('-title')[:]))
    context_1 = {
        "obj": Product.objects.order_by('-title')[:],
    }
    return render(request, template_name='home.html', context = context_1 )


def product(request, pk = None):
    if pk:
        obj = Product.objects.filter(id = pk)[0]
        return render(request, template_name="product.html", context ={"obj":obj} )

    else:
        return redirect('home')

def buy(request, pk = None):
    user = request.user
    product_obj = Product.objects.filter(id = pk)[0]
    product_obj.users.add(user)
    return home(request)

def checkout(request, pk = None):
    if pk:
        obj = Product.objects.filter(id = pk)[0]
        return render(request, template_name="checkout.html", context ={ "obj" : obj } )
    else:
        return redirect('home')

def user_purchases(request):
    user_id = request.user.pk
    objs = []
    for item in Product.objects.filter():
        if item.users.filter(id = user_id):
            objs.append(item)
    obj = Product.objects.filter()
        
        # obj.pop(obj.index(item))

    print(22222222222222222222222222222222222222222222222222, obj)
    # for i in obj:
    #     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', i)
    return render(request, template_name="home.html", context ={ "obj" : obj } )