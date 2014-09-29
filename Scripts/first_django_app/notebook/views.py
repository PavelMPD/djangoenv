import json

from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.defaultfilters import safe


def view(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('notebook.html', args)


def save(request):
    if request.method == 'POST':
        result = True
    data = json.loads(request.body.decode())
    #return HttpResponse(json.dumps({'result': result}), content_type="application/json")
    #return JsonResponse({'result': result})
    return HttpResponse("OK")


def load(request):
    data = [{u'status': 0, u'description': u'New note', u'ord': 0}, {u'status': 0, u'description': u'New note2', u'ord': 0}]
    return JsonResponse(data, safe=False)