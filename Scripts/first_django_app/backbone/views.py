from django.shortcuts import render_to_response


def bbevents(request):
    return render_to_response('bbevents.html')


def bbmodel(request):
    return render_to_response('bbmodel.html')


def utemplate(request):
    return render_to_response('utemplate.html')


def bbview(request):
    return render_to_response('bbview.html')


def bbcollection(request):
    return render_to_response('bbcollection.html')


def bbcollection2(request):
    return render_to_response('bbcollection2.html')