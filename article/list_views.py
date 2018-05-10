#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-7 下午7:27
# @Author  : GodFather
# @Email   : liuyuhang791034063@qq.com
# @File    : list_views.py
# @Software: PyCharm
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import redis
from django.conf import settings

from .models import ArticlePost,ArticleColumn,Comment
from .forms import CommentForm

r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

def article_titles(request,username=None):
    if username:
        user = User.objects.get(username=username)
        articles_title = ArticlePost.objects.filter(author=user)
        try:
            userinfo = user.userinfo
        except:
            userinfo = None
    else:
        articles_title = ArticlePost.objects.all()
    paginator = Paginator(articles_title, 5)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    if username:
        return render(request, "article/list/author_articles.html",{"articles":articles,"page":current_page,"userinfo":userinfo,"user":user})
    return render(request, "article/list/article_titles.html",{"articles":articles,"page":current_page})

def article_detail(request, id, slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    total_views = r.incr("article:{}:views".format(article.id))
    r.zincrby('article_ranking',article.id,1)

    article_ranking = r.zrange('article_ranking',0,-1,desc=True)
    article_ranking_dis = [int(id) for id in article_ranking]
    most_viewed = list(ArticlePost.objects.filter(id__in = article_ranking_dis))
    most_viewed.sort(key= lambda x:article_ranking_dis.index(x.id))

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, "article/list/articlel_detail.html", {"article":article,
                                                                 "total_views":total_views,
                                                                 "most_viewed":most_viewed,
                                                                 "comment_form":comment_form})

@csrf_exempt
@require_POST
@login_required(login_url='/account/login/')
def like_article(request):
    article_id = request.POST.get("id")
    action = request.POST.get("action")
    if article_id and action:
        try:
            article = ArticlePost.objects.get(id=article_id)
            if action == "like":
                article.users_like.add(request.user)
                return HttpResponse("1")
            else:
                article.users_like.remove(request.user)
                return HttpResponse("2")
        except:
            return HttpResponse("no")