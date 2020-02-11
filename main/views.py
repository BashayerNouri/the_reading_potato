from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
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