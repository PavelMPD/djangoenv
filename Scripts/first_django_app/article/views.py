from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
from django.core.context_processors import csrf

# Create your views here.
def basic_one(request):
    view = "basic_one"
    html = "<html><body>First page {}</body></html>".format(view)
    return HttpResponse(html)


def first_view(request):
    view = 'First view from template'
    t = get_template('first_view.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)


def second_view(request):
    view = 'Second view from template'
    return render_to_response('first_view.html', {'name': view})


def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})


def article(request, id=1):
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=id)
    args['comments'] = Comments.objects.filter(article_id=id)
    args['form'] = CommentForm()
    return render_to_response('article.html', args)


def addlike(request, id):
    try:
        article = Article.objects.get(id=id)
        if id in request.COOKIES:
            article.likes -= 1
        else:
            article.likes += 1
        article.save()
        response = redirect('/articles/all')
        response.set_cookie(id, 'test')
        return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/articles/all')


def addcomment(request, id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = Article.objects.get(id=id)
            comment.save()
            request.session.set_expiry(30)
            request.session['pause'] = True
    return redirect('/articles/get/{}'.format(id))

