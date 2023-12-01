from django.shortcuts import render

from . models import Category , Product

from django.shortcuts import get_object_or_404

from django.db.models import Q
# Create your views here.


def store(request) :
  
  all_products = Product.objects.all()

  context ={'my_products': all_products}

  return render(request,'store/store.html',context)

def categories(request):

  all_categories = Category.objects.all()

  return {'all_categories': all_categories}


def list_category(request,category_slug=None):
  
  category = get_object_or_404(Category,slug=category_slug)

  products = Product.objects.filter (category= category)

  return render (request,'store/list-category.html',{'category' : category, 'products' : products})

  


# Product describe
def product_info(request, product_slug):

  product = get_object_or_404(Product, slug= product_slug)

  context = {'product' : product}

  return render(request, 'store/product-info.html',context)


def search_products(request):
    query = request.GET.get('q')
    if query:
        # Search for products that contain the query in their title or description
        products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        context = {'query': query, 'products': products}
        return render(request, 'store/search-results.html', context)
    else:
        # If no query is provided, display all products
        all_products = Product.objects.all()
        context = {'my_products': all_products}
        return render(request, 'store/store.html', context)

