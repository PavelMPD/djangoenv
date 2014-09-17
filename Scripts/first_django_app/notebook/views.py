from django.shortcuts import render_to_response


def simpleone(request):
    return render_to_response('simpleone.html')


def view(request):
    return render_to_response('notebook.html')


def edit(request):
    return render_to_response('notebook.html')