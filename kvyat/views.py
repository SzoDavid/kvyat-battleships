from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


def create(request):
    context = {'selected': 'create'}
    return render(request, 'kvyat/create.html', context)


def join(request, room_id):
    context = {'room_id': room_id,
               'url': request.get_full_path()}
    return render(request, 'kvyat/join.html', context)


def temp_guest(request, room_id):
    context = {'room_id': room_id}
    return render(request, 'kvyat/temp_join_guest.html', context)


def room(request, room_id):
    context = {'room_id': room_id}
    return render(request, 'kvyat/room.html', context)


def top(request):
    context = {'selected': 'top'}
    return render(request, 'kvyat/top.html', context)


def profile(request, user_id):
    context = {
        'selected': 'profile',
        'profile': get_object_or_404(User, pk=user_id)}
    return render(request, 'kvyat/profile.html', context)


def about(request):
    context = {'selected': 'about'}
    return render(request, 'kvyat/about.html', context)


def creator(request):
    context = {'selected': 'creator'}
    return render(request, 'kvyat/creator.html', context)


def contact(request):
    context = {'selected': 'contact'}
    return render(request, 'kvyat/contact.html', context)


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password_again']

        if password1 != password2:
            return render(request, 'kvyat/register.html', {
                'error': 'Are you an idiot? You wrote two different passwords...',
                'username': username,
                'email': email})

        if User.objects.filter(username=username).count() != 0:
            return render(request, 'kvyat/register.html', {
                'error': 'Try to be creative, this username is already taken',
                'email': email})

        if User.objects.filter(email=email).count() != 0:
            return render(request, 'kvyat/register.html', {
                'error': 'You\'ve already registered with this email address',
                'username': username})

        try:
            validate_password(password1)
        except ValidationError:
            return render(request, 'kvyat/register.html', {
                'error': 'C\'mon, you surly can come up with something stronger...',
                'username': username,
                'email': email})

        user = User.objects.create_user(username, email, password1)
        login(request, user)
        return redirect(reverse('kvyat:create'))
    else:
        return render(request, 'kvyat/register.html')


def create_room(request):
    return


def remove_room(request, room_id):
    return


def create_user(request):
    return


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('kvyat:create'))
    else:
        # Return an 'invalid login' error message.
        return


def logout_user(request, user_id):
    logout(request)
    return HttpResponseRedirect(reverse('kvyat:create'))
