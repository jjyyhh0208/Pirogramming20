from django.shortcuts import render, redirect
from .models import DevTool
from .forms import DevToolForm
from ..ideas.models import Idea


# Create your views here.
def tool_list (request):
    devtools = DevTool.objects.all()
    ctx = {
        'devtools' : devtools
    }
    return render(request, 'devtools/devtool_list.html', ctx)

def tool_create (request):
    if request.method == 'GET':
        forms = DevToolForm()
        ctx = {
            'forms' : forms
        }
        return render(request, 'devtools/devtool_create.html', ctx)
    forms = DevToolForm(request.POST)
    if forms.is_valid():
        forms.save()
    return redirect('devtools:list')

def tool_detail (request, pk):
    devtool = DevTool.objects.get(id=pk)
    related_ideas = Idea.objects.filter(tool=devtool)
    ctx = {
        'devtool' : devtool,
        'pk' : pk,
        'related_ideas' : related_ideas
    }
    return render(request, 'devtools/devtool_detail.html', ctx)

def tool_delete (request, pk):
    if request.method == 'POST':
        devtool = DevTool.objects.get(id=pk).delete()
    return redirect('devtools:list')

def tool_update (request, pk):
    devtool = DevTool.objects.get(id=pk)
    if request.method == 'GET':
        forms = DevToolForm(instance=devtool)
        ctx = {
            'forms' : forms,
            'pk' : pk
        }
        return render(request, 'devtools/devtool_update.html', ctx)
    forms = DevToolForm(request.POST, instance=devtool)
    if forms.is_valid():
        forms.save()
    return redirect('devtools:detail', pk)