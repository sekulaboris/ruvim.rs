from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, \
                    UserEditForm, ProfileEditForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Profile
from orders.models import Order

@staff_member_required
def admin_order_detail(request, order_id):
    order= get_object_or_404(Order, id=order_id)
    return render (request,
                   'orders_detail.html',
                    {'order':order})


def loged_in(request):
    messages.success(request, ('Uspesno ste se ulogovali.'))
    return render(request, 'loged_in.html', {})

def login_user(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('account:loged_in')
                else:
                    return HttpResponse('Disable account')
            else:
                messages.error(request, 'Niste registrovan clan!')
                return redirect('account:login_user')
    else:
        form=LoginForm()
    return render (request, 'login.html', { 'form': form })
# Create your views here.

@login_required()
def logged_out(request):
    logout(request)
    messages.success(request, ('Uspesno ste se izlogovali.'))
    return render(request, 'logged_out.html', {})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                        'account/register_done.html',
                        { 'user_form': user_form })
    else:
        user_form= UserRegistrationForm()
    return render (request,
                    'account/register.html',
                    {'user_form': user_form})

@login_required
def edit(request):
    if request.method=='POST':
        user_form= UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form= ProfileEditForm(instance=request.user.profile,
                                        data= request.POST,
                                        files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated'\
                                        'successfully')
    else:
        user_form= UserEditForm(instance=request.user)
        profile_form= ProfileEditForm(instance=request.user.profile)
        messages.error(request, 'Error updating your profile')
    return render(request,
                    'account/edit.html',
                    {'user_form':user_form,
                    'profile_form':profile_form})

