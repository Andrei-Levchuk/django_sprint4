from django.shortcuts import render
from django.utils import timezone

from .utils import (get_published_posts,
                    paginate_posts,
                    get_published_post_or_404,
                    get_published_category_or_404)


def index(request):
    posts = get_published_posts()
    posts = paginate_posts(posts, page_number=1)
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_published_post_or_404(post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_published_category_or_404(category_slug)
    post_list = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)
