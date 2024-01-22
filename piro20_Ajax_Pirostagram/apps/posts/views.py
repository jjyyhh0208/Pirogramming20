from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import json

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
            post.like = 0
            post.save()
        return redirect('posts:main')
        
    else:
        form = NewPost()
        ctx = {
            'form' : form
        }
        return render(request, 'posts/post_create.html', ctx)
    
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.all()
    ctx = {
        'post' : post,
        'comments' : comments,
        'pk' : pk
    }
    return render(request, 'posts/post_detail.html', ctx)


def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        post.delete()
        return redirect('posts:main')
    
def post_update(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = NewPost(request.POST, instance=post)
        if form.is_valid:
            form.save()
        return redirect('posts:detail', pk=pk)
    else:
        form = NewPost(instance=post)
        ctx = {
            'form' : form,
            'pk' : pk
        }
        return render(request, 'posts/post_update.html', ctx)
    
def addComment (request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = NewComment(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return render('posts:detail, pk')
    else:
        form = NewComment()
        ctx ={
            'form' : form
        }
    return render(request, 'add_comment.html', ctx)

@csrf_exempt
def like_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            post_id = data.get('id')
            post = Post.objects.get(id=post_id)
            post.is_liked = not post.is_liked  # Toggle the like status
            post.save()
            return JsonResponse({'id': post_id, 'isLiked': post.is_liked})
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
@csrf_exempt
def addComment(request, pk):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            post = Post.objects.get(id=pk)
            comment_content = data['content']
            commenter = request.user  # 현재 로그인한 사용자

            comment = Comment.objects.create(post=post, content=comment_content, commenter=commenter)
            return JsonResponse({'id': comment.id, 'content': comment.content, 'commenter': comment.commenter.username})
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
def delete_comment(request, comment_id):
    if request.method == 'DELETE':
        try:
            comment = Comment.objects.get(id=comment_id, commenter=request.user)
            comment.delete()
            return JsonResponse({'status': 'success'})
        except Comment.DoesNotExist:
            return JsonResponse({'error': 'Comment not found or not allowed to delete'}, status=404)
    else:
        return HttpResponseForbidden('Invalid request method')