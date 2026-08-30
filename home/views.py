from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Contact
from django.contrib import messages

# Create your views here.



def index(request):

    success = False

    if request.method == "POST":

        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            message=request.POST.get("message"),
        )

        success = True

    featured_products = Product.objects.filter(
        is_featured=True,
        is_available=True
    )[:6]

    return render(
        request,
        "home/index.html",
        {
            "products": featured_products,
            "success": success,
        }
    )



def product_detail(request, slug):

    product = get_object_or_404(
        Product,
        slug=slug,
        is_available=True
    )

    related_products = Product.objects.filter(
        category=product.category,
        is_available=True
    ).exclude(id=product.id)[:4]

    context = {
        "product": product,
        "related_products": related_products,
    }

    return render(
        request,
        "home/product_detail.html",
        context,
    )



def contact(request):
    return render(request,"home/contactNP.html")