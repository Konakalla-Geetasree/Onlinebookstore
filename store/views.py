from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.

def store(request, category_slug=None):
    categories=None
    products = None

    if category_slug !=  None:
        categories=get_object_or_404(Category,slug=category_slug)
        products= Product.objects.filter(category=categories,is_available=True)
        product_count=products.count()
    else:
        products=Product.objects.all().filter(is_available=True)
        product_count=products.count()

    context={
        'products': products,
        'product_count' : products.count,

    }
    return render(request,'store/store.html',context)

def product_detail(request, category_slug, product_slug):
    try:
        # Get the Category instance corresponding to the category_slug
        category = get_object_or_404(Category, slug=category_slug)
        # Now, filter Product objects based on both category and product_slug
        single_product = get_object_or_404(Product, category=category, slug=product_slug)

    except Exception as e:
        # It's better to be more specific about the exception you're catching
        raise e
    
    context = {
        'single_product': single_product,
    }

    return render(request, 'store/product_detail.html', context)
