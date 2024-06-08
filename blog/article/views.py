from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User

from article.models import Article
from article.forms import ArticleForm


def list_article(request):
    articles = get_list_or_404(Article)
    
    return render(request,"article_list.html",context={'articles':articles})

    
    
def add_article(request):
    user = User.objects.get(username='admin')
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid:
            form.instance.author = user
            form.save()
            return redirect('list_article')
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', context={'form':form})
    
    
def article(request, id):
    article = Article.objects.get(id=id)
    return render(request, "article.html", context={'article':article})


def article_update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('article', id=id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_update.html', context={'form':form})


def article_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('list_article')

    