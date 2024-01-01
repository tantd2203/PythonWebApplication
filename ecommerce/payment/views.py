
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .models import ShippingAddress,Order,OrderItem

from cart.cart import Cart


def payment_success(request):

    return render(request,'payment/payment-success.html')


def payment_failed(request):

    return render(request,'payment/payment-failed.html')




def checkout(request):


    if request.user.is_authenticated:

        try:

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


        if request.user.is_authenticated:

            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address,
            
            amount_paid=total_cost, user=request.user)
            order_id = order.pk

            for item in cart:

                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'],
                
                price=item['price'], user=request.user)
            
            # mail success payment
            # order_mail = Order.objects.filter(id=order_id)
            # order_items_list = []  
            # for order in order_mail:
            #     order_items = OrderItem.objects.filter(order=order)
                
            #     order_items_list.append({
            #         'order': order,
            #         'order_items': order_items,
            #     })

            # context = {
            #     'order_items_list': order_items_list,
            # }
            # # render gmail
            # # Email verification setup (template)
            # current_site = get_current_history_length(request)
            # subject = 'Payment success   email'
            # message = render_to_string('payment/mailpayment.html',context=context)
            # to_email = request.user.email  # Assuming user is logged in
            # email = EmailMessage(subject, message, to=[to_email])
            # #  Unable to connect 
            # request.user.email_user(message=message,subject= subject)


                
    #  2) Create order -> Guest users without an account

        else:

            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address,
            
            amount_paid=total_cost)


            order_id = order.pk


            for item in cart:

                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'],
                
                price=item['price'])
            
            # order_mail = Order.objects.filter(id=order_id)
            # order_items_list = []  
            # for order in order_mail:
            #     order_items = OrderItem.objects.filter(order=order)
                
            #     order_items_list.append({
            #         'order': order,
            #         'order_items': order_items,
            #     })

            # context = {
            #     'order_items_list': order_items_list,
            # }
            # # render gmail
            # # Email verification setup (template)
            # current_site = get_current_history_length(request)
            # subject = 'Payment success   email'
            # message = render_to_string('payment/mailpayment.html',context=context)
            # to_email = request.user.email  # Assuming user is logged in
            # email = EmailMessage(subject, message, to=[to_email])
            # #  Unable to connect 
            # request.user.email_user(message=message,subject= subject)

        order_success = True


        response = JsonResponse({'success':order_success})

        return response






    




def payment_success(request):

    for key in list(request.session.keys()):

        if key == 'session_key':

            del request.session[key]

    return render(request, 'payment/payment-success.html')


def payment_failed(request):

    return render(request, 'payment/payment-failed.html')







