from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib import auth
from django.core.context_processors import csrf


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/articles/all')
        else:
            args['login_error'] = 'User does not exist'
            return render_to_response('login.html', args)
    return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/articles/all')