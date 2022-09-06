from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegister

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('entry-list')      
    else:
        form = UserRegister()
    return render(request, 'users/register.html', {'form':form})

