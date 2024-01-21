from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
def main (request):
    posts = Post.objects.filter(writer = request.user)
    ctx = {
        'posts' : posts
    }
    return render(request, 'users/main.html', ctx)

def post_create(request):
    if request.method == 'POST':
        form = NewPost(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.writer = request.user
            post.save()
        return redirect('posts:main')
        
    else:
        form = NewPost(initial={'writer': request.user})
        ctx = {
            'form' : form
        }
        return render(request, 'posts/post_create.html', ctx)
    
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    ctx = {
        'post' : post,
        'pk' : pk
    }
    return render(request, 'posts/post_detail.html', ctx)


def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        post.delete()
        return redirect('posts:main')
    
def post_update(request, pk):
    pass