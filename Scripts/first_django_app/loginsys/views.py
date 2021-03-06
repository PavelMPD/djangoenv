from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/articles/all/')
        else:
            args['login_error'] = 'User does not exist'
            return render_to_response('login.html', args)
    return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/articles/all')


def registration(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            username=newuser_form.cleaned_data['username']
            password=newuser_form.cleaned_data['password2']
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('/articles/all/')
        else:
            args['form'] = newuser_form
    return render_to_response('registration.html', args)