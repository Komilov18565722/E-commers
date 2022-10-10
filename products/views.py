from django.shortcuts import redirect, render
from .models import Product
from django.contrib import messages
import datetime
# Create your views here.

def add_prodect(request):
    print("11111111111111111111111111111", request.user)
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