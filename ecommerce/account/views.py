from django.shortcuts import render, redirect


from .forms import CreateUseForm



def register(request): 

     form = CreateUseForm()

     if request.method == 'POST':
          
          form = CreateUseForm(request.POST)

          if form.is_valid():

               form.save()

               return redirect('store')

     context = {'form': form}
 
     return  render(request,'account/registration/register.html', context= context)

# # Create your views here.

# def email_verification(request, uidb64, token):



def email_verification_sent(request):

    return render(request, 'account/registration/email-verification-sent.html')


def email_verification_success(request):

    return render(request, 'account/registration/email-verification-success.html')



def email_verification_failed(request):

    return render(request, 'account/registration/email-verification-failed.html')
