from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from kvyat.models import UserData


def home(request):
    context = {'selected': 'home'}
    return render(request, 'kvyat/home.html', context)


@login_required(login_url='/kvyat/login/')
def room(request):
    return render(request, 'kvyat/room.html')


def profile(request, user_id):
    _profile = get_object_or_404(User, pk=user_id)
    context = {
        'selected': 'profile',
        'profile': _profile,
        'profile_data': _profile.userdata_set.get(user=_profile)}
    return render(request, 'kvyat/profile.html', context)


def about(request):
    context = {'selected': 'about'}
    return render(request, 'kvyat/about.html', context)


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
        UserData.objects.create(user=user)
        login(request, user)
        return redirect(reverse('kvyat:home'))
    else:
        return render(request, 'kvyat/register.html')


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('kvyat:home'))
    else:
        return HttpResponseRedirect(reverse('kvyat:login'))


def upload_points(request, user_id, guesses):
    user = get_object_or_404(User, pk=user_id)
    data = user.userdata_set.get(user=user)
    data.games_played += 1
    data.guesses += guesses
    data.save()
    return HttpResponseRedirect(reverse('kvyat:home'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('kvyat:home'))
