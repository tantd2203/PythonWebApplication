from django.shortcuts import render

from . models import Category , Product

from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q


def store(request):
    all_products = Product.objects.all()
    items_per_page = 5
    paginator = Paginator(all_products, items_per_page)
    page = request.GET.get('page')

    try:
        my_products = paginator.page(page)
    except PageNotAnInteger:
        my_products = paginator.page(1)
    except EmptyPage:
        my_products = paginator.page(paginator.num_pages)

    context = {'my_products': my_products}
    return render(request, 'store/store.html', context)

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

       products = Product.objects.filter(Q(title__contains=query) | Q(description__contains=query))
       context = {'query': query, 'products': products}
       return render(request, 'store/search-results.html', context)
    else:
        
        all_products = Product.objects.all()
        context = {'my_products': all_products}
        return render(request, 'store/store.html', context)



def sort_product(request):
   queryset = Product.objects.all()
   sort_by = request.GET.get('sort_by')
   if sort_by == 'title' :
      queryset =queryset.order_by('title')
   elif sort_by == 'price':
      queryset =queryset.order_by('price')

   return render(request, 'store/product-sort.html',{'products':queryset})
   
