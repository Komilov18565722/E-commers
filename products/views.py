from django.shortcuts import redirect, render
from .models import Product
from django.contrib import messages
import datetime
# Create your views here.

def add_prodect(request):
    # print("11111111111111111111111111111", request.user)
    if request.user.is_superuser:
        
        if request.method == "POST":
            try:
            
                title = request.POST['title']
                bio = request.POST['bio']
                deff = request.POST['deff']
                price = request.POST['price']
                count = request.POST['count']
                dprice = request.POST['dprice']
                photo1 = request.FILES['photo1']
                photo2 = request.FILES.get('photo2')
                photo3 = request.FILES.get('photo3')
                photo4 = request.FILES.get('photo4')

                product = Product(
                    title = title,
                    bio = bio,
                    definition = deff,
                    price = price,
                    count = count,
                    delivery_price = dprice,
                    photo1 = photo1,
                    photo2 = photo2,
                    photo3 = photo3,
                    photo4 = photo4,
                )
                
                product.save()

                messages.success(request, ("Success : The product has been successfully added"),)
            except:
                messages.warning(request, ("Error : There was an error adding the product. Please try again"),)
            return redirect('home')
        
             
        else:
            return render(request, template_name='add_product.html')
    else:
        return redirect('home')

def delete_product(request, pk=None):
    if request.user.is_superuser and pk:
        if pk:
            product = Product.objects.filter(pk = pk)[0]
            if product:
                Product.delete(product)
                messages.success(request, ("Products delete successful"),)
            else:
                messages.warning(request, ("Not found pk, please try again"),)    
                return redirect(request, ("Not found product, please try again"))
        else:
            messages.success(request, ("Not found pk, please try again"),)
        return redirect('home')
    else:
        return redirect('home')

def update_product(request, pk = None):
    if request.user.is_superuser:
        if request.method == "GET":
            product = Product.objects.get(pk = pk)
            return render(request, 'update_product.html', {"obj" : product})
        elif request.method == "POST":
            # try:
            product = Product.objects.get(pk=pk)
            if request.POST['title']:
                product.title = request.POST['title']
            if request.POST['bio']:
                product.bio = request.POST['bio']
            if request.POST['deff']:
                product.definition = request.POST['deff']
            if request.POST['price']:
                product.price = request.POST['price']
            if request.POST['count']:
                product.count = request.POST['count']
            if request.POST['dprice']:
                product.delivery_price = request.POST['dprice']
            if request.FILES.get('photo1'):
                product.photo1 = request.FILES['photo1']
            if request.FILES.get('photo2'):
                product.photo2 = request.FILES.get('photo2')
            if request.FILES.get('photo3'):
                product.photo3 = request.FILES.get('photo3')
            if request.FILES.get('photo4'):
                product.photo4 = request.FILES.get('photo4')
            
            product.save()
            #     messages.success(request, ("Success edited product"))
            # except:
            #     messages.warning(request, ("Error: edited product, please try again"))
            return redirect('home')

