from django.urls import path

from .import views

urlpatterns = [

    path('', views.store, name='store'),

    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
    
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
    
    path('search1/', views.search_products, name='search_products'),

    path('sort/', views.sort_product, name='sort'),


]