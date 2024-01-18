from django.shortcuts import render, redirect, get_object_or_404
from .models import Idea
from .forms import IdeaForm

# Create your views here.
def main (request):
    ideas = Idea.objects.all()
    ctx = {
        'ideas' : ideas,
    }
    return render(request, 'ideas/idea_main.html', ctx)

def detail(request, pk):
    idea = Idea.objects.get(id=pk)
    ctx = {
        'idea' : idea,
        'pk' : pk
    }
    return render(request, 'ideas/idea_detail.html', ctx)

def create (request):
    if request.method == 'GET':
        forms = IdeaForm()
        ctx = {
            'forms' : forms
        }
        return render(request, 'ideas/idea_create.html', ctx)
    forms = IdeaForm(request.POST, request.FILES)
    if forms.is_valid():
        forms.save()
    return redirect('ideas:main')

def delete(request, pk):
    if request.method == 'POST':
        idea = Idea.objects.get(id=pk).delete()
    return redirect('ideas:main')

def update(request, pk):
    idea = Idea.objects.get(id=pk)
    if request.method == 'GET':
        forms = IdeaForm(instance=idea)
        ctx = {
            'forms' : forms,
            'pk' : pk
        }
        return render(request, 'ideas/idea_update.html', ctx)
    
    forms = IdeaForm(request.POST, request.FILES, instance=idea)
    if forms.is_valid():
        forms.save()
    return redirect('ideas:detail', pk)

def increase_interest(request, id):
    idea = get_object_or_404(Idea, id=id)
    idea.interest += 1
    idea.save()
    return redirect('ideas:main')

def decrease_interest(request, id):
    idea = get_object_or_404(Idea, id=id)
    idea.interest -= 1
    idea.save()
    return redirect('ideas:main')

def my_list_view(request):
    sort = request.GET.get('sort', 'default')

    if sort == 'title':
        ideas = Idea.objects.order_by('title')
    elif sort == 'date':
        ideas = Idea.objects.order_by('created_date')
    elif sort == 'new':
        ideas = Idea.objects.order_by('-created_date')
    else:
        ideas = Idea.objects.all()

    ctx = {
        'ideas' : ideas
    }
    return render(request, 'ideas/idea_main.html', ctx)