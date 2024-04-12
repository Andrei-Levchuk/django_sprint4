from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Category, Post


def get_published_posts():
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def paginate_posts(posts, page_number, per_page=5):
    paginator = Paginator(posts, per_page)
    return paginator.page(page_number)


def get_published_post_or_404(post_id):
    return get_object_or_404(
        get_published_posts(),
        pk=post_id
    )


def get_published_category_or_404(category_slug):
    return get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
