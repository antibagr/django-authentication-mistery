import os

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AccountCreationForm, AccountUpdateForm
from .models import User
from typehints import HttpResponse, RequestType
from verbose import msg


__all__ = ['sign_up', 'custom_logout', 'profile', 'change_password']


@login_required
def home(request: RequestType) -> HttpResponse:
    return render(request, 'account/home.html')


def about(request: RequestType) -> HttpResponse:
    return render(request, 'account/about.html')


def sign_up(request: RequestType) -> HttpResponse:

    form = AccountCreationForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            messages.success(request, msg.new_user_created)
            form.save()
            return redirect('login')

        messages.warning(request, msg.error.form_error)

    return render(request, 'account/sign_up.html', {'form': form})


@login_required
def custom_logout(request: RequestType) -> HttpResponse:

    messages.success(request, msg.logged_out)

    return auth_views.LogoutView.as_view(template_name='account/logout.html')(request)


@login_required
def profile(request: RequestType) -> HttpResponse:

    form = AccountUpdateForm(request.POST or None, instance=request.user)

    if request.method == 'POST':

        print(request.FILES)

        print(form.is_valid())

        if form.is_valid():
        #  and form.has_changed():

            if request.FILES.get('image', None) is not None:

                try:
                    os.remove(request.user.avatar.url)
                except Exception as e:
                    print('Exception in removing old profile image: ', e)

                request.user.image = request.FILES['image']
                request.user.save()

            form.save()

            messages.success(request, msg.updated)

        return redirect('account_profile')

    return render(request, 'account/profile.html', {'form': form})


@login_required
def change_password(request: RequestType) -> HttpResponse:

    form = PasswordChangeForm(request.user, request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user = form.save()

            # Important!
            update_session_auth_hash(request, user)

            messages.success(request, msg.password_updated)

            return redirect('change_password')

        messages.error(request, 'Please correct the error below.')

    return render(request, 'account/change_password.html', {'form': form})
