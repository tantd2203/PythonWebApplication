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

# Create your views here.
