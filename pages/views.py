from django.shortcuts import render, redirect
from products.models import Product

# Create your views here.

def home(request):
    context_1 = {
        "obj": Product.objects.order_by('-title')[:],
    }
    return render(request, template_name='home.html', context = context_1 )


def product(request, pk = None):
    print(111111111111111111111111111, pk)
    if pk:
        obj = Product.objects.filter(id = pk)[0]
        # print(1111111111111111111111111111111111111111111111111111111111111111, (obj[0]))
        return render(request, template_name="product.html", context ={"obj":obj} )
    else:
        return redirect('home')