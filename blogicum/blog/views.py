from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from datetime import datetime


def get_posts(post_objects):
    """Функция для получения поста/ов из базы данных."""
    return post_objects.select_related(
        'location',
        'author',
        'category'
    ).filter(
        pub_date__lt=datetime.now(),
        is_published=True
    )


def index(request):
    """View-функция для обработки запроса к главной странице."""
    template = 'blog/index.html'
    post_list = get_posts(Post.objects).filter(
        category__is_published=True
    ).order_by('pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def category_posts(request, category_slug):
    """View-функция для обработки запроса к странице с постами по категории."""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug, is_published=True)
    # так не работает, у category нет такого атрибута:
    # post_list = get_posts(category.posts)
    post_list = get_posts(Post.objects).filter(
        category=category, pub_date__lt=datetime.now())
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    """View-функция для обработки запроса к странице отдельного поста."""
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        id=post_id,
        pub_date__lt=datetime.now(),
        is_published=True,
        category__is_published=True
    )
    context = {'post': post}
    return render(request, template, context)
