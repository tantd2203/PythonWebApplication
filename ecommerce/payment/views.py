from django.http import JsonResponse
from django.shortcuts import render

from .models import ShippingAddress,Order,OrderItem

from cart.cart import Cart

# Create your views here.


def payment_success(request):

    return render(request,'payment/payment-success.html')


def payment_failed(request):

    return render(request,'payment/payment-failed.html')




def checkout(request):

    # Users with accounts fill the form

    if request.user.is_authenticated:

        try:
            # Authenticated user WITH shipping  information

            shipping_address = ShippingAddress.objects.get(user = request.user.id)

            context= {'shipping' : shipping_address}

            return render (request, 'payment/checkout.html',context=context)
        
        except:
            # Authenticated users with NO shipping information

                return render (request, 'payment/checkout.html')
        


    else:

        # Guest user
        return render(request,'payment/checkout.html')
    


def complete_order(request):

    if request.POST.get('action') == 'post':

        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')

        shipping_address = (address +"\n" +
        
        city )



         # Shopping cart information 

        cart = Cart(request)

        # Get the total price of items

        total_cost = cart.get_total()


         # 1) Create order -> Account users WITH + WITHOUT shipping information

        if request.user.is_authenticated:

            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address,
            
            amount_paid=total_cost, user=request.user)


            order_id = order.pk

            for item in cart:

                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'],
                
                price=item['price'], user=request.user)
                
    #  2) Create order -> Guest users without an account

        else:

            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address,
            
            amount_paid=total_cost)


            order_id = order.pk


            for item in cart:

                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'],
                
                price=item['price'])



        order_success = True

        response = JsonResponse({'success':order_success})

        return response






    




def payment_success(request):


    # Clear shopping cart


    for key in list(request.session.keys()):

        if key == 'session_key':

            del request.session[key]



    return render(request, 'payment/payment-success.html')






def payment_failed(request):

    return render(request, 'payment/payment-failed.html')







