from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Tag
from django.core.paginator import Paginator
from .forms import MessageForm

# Create your views here.


def home(request):
    latest_articles = Article.objects.filter(active=True).order_by('-created')[:3]
    popular_articles = Article.objects.filter(active=True).order_by('-views')[:3]
    tags = Tag.objects.all()
    return render(request, 'blog/home.html', {'latest_articles': latest_articles, 'popular_articles': popular_articles, 'tags': tags})


def article_detail(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    articles.views += 1
    articles.save()
    return render(request, 'blog/article_detail.html', {'articles': articles})


def article_list(request):
    articles = Article.objects.filter(active=True)
    tags = Tag.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 4)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', {'articles': object_list, 'tags': tags})


def article_tag(request, tag_id):
    tags = Tag.objects.all()
    active_tag = get_object_or_404(Tag, id=tag_id)
    articles = active_tag.articles.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 4)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/article_tag.html', {'tags': tags, 'active_tag': active_tag, 'articles': object_list})


def search(request):
    article_search = request.GET.get('search')
    articles = Article.objects.filter(title__icontains=article_search)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 4)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', {'articles': object_list})


def about(request):
    return render(request, 'blog/about_me.html')


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = MessageForm()
    return render(request, 'blog/contact_me.html', {'form': form})

