from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.

def articles_list(request):
    article = Article.objects.all()
    paginator = Paginator(article, 5) # Shows up to 5 articles per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {
        "articles" : articles,
        "page" : page,
    }
    return render(request, "articles_list.html", context)


def article_details(request, article_id):
	article = Article.objects.get(id=article_id)
	context = { 
	"article" : article,
	}
	return render(request, 'article_details.html', context)


def create_article(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article-details', article.id)

    context = {"form" : form}

    return render(request, "create_article.html", context)


def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)

    form = ArticleForm(instance=article)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('article-details', article_id)

    context = {"form":form, "article":article}
    return render(request, 'edit_article.html', context)


def my_articles_list(request):
    return render(request, "my_articles_list.html")

    