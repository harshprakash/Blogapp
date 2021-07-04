from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisteration,UserUpdateform,ProfileUpdateform
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisteration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"your account is created now you can login !")
            return redirect('Login')
    else:    
        form = UserRegisteration()
    return render(request,"users/registeration.html",{'form':form})
@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateform(request.POST,instance=request.user)
        p_form=ProfileUpdateform(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
             u_form.save()
             p_form.save()
             messages.success(request,f"your profile has been updated !")
             return redirect('profile')


    else:
        u_form=UserUpdateform(instance=request.user)
        p_form=ProfileUpdateform(instance=request.user.profile)

    
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,"users/profile.html",context)