from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.

def home_index(request):
    return render(request, 'index.html')


def home_steinbeck(request):
    return render(request, 'blog/steinbeck.html')

def home_blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/post.html', {'posts': posts})

def home_detail(request, id):
    post  = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context)


def home_grid(request):
    return render(request, 'grid.html')