from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
def main (request):
    posts = Post.objects.get(writer = request.user)
    ctx = {
        'posts' : posts
    }
    return render(request, 'users/main.html', ctx)

def post_create(request):
    form = NewPost()
    if request.method == 'POST':
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:main')
        else:
            return render(request, 'test.html')
    else:
        form = NewPost(initial={'writer': request.user})
        ctx = {
            'form' : form
        }
        return render(request, 'posts/post_create.html', ctx)