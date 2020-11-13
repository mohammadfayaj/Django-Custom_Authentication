from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, AddressForm
from.models import Profile, Address


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    photos = Profile.objects.all()
    if request.method == "POST":
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('users-profile')
    else:
        pass
    form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'form': form,
        'photos': photos,
    }
    return render(request, 'users/profile.html', context)


@login_required
def profile_info(request):
    photos = Profile.objects.all()
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        if user_update_form.is_valid():
            user_update_form.save()
            return redirect('users-profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)

    context = {
        "user_update_form": user_update_form,
        "photos": photos

    }
    return render(request, 'users/profile_info.html', context)


@login_required
def address_info(request):
    address_info_list = Address.objects.all()
    if request.method == "POST":
        address_info_form = AddressForm(request.POST, instance=request.user.address)
        if address_info_form.is_valid():
            address_info_form.save()
            return redirect('users-profile')
    else:
        address_info_form = AddressForm(instance=request.user.address)
    context = {
        "address_info_list": address_info_list,
        "address_info_form": address_info_form
    }
    return render(request, 'users/address_info.html', context)
