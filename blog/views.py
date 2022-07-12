from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def blog(request):
    posts = Article.objects
    return render(request, 'blog/blog.html', {'article': posts})


def specific_post(request, post_id):
    post = get_object_or_404(Article, pk=post_id)
    return render(request, 'blog/post.html', {'post': post})