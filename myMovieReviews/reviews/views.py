from django.shortcuts import render, redirect
from .models import Reviews
from datetime import datetime, time

# Create your views here.
def reviews_list(request):
    reviews = Reviews.objects.order_by('createdDate')
    context = {
        "reviews" : reviews
    }
    return render(request, 'reviews_list.html', context)

def reviews_read(request, pk):
    review = Reviews.objects.get(id=pk)
    context = {
        "review" : review
    }
    return render(request, 'reviews_read.html', context)

def reviews_create(request):
    if request.method == 'POST':
        Reviews.objects.create(
            title = request.POST["title"],
            createdDate = request.POST["createdDate"],
            genre = request.POST["genre"],
            rank = request.POST["rank"],
            running_time = request.POST["running_time"],
            content = request.POST["content"],
            director = request.POST["director"],
            actors = request.POST["actors"],
        )
        return redirect("/")
    return render(request, 'reviews_create.html')

def reviews_delete(request, pk):
    if request.method == "POST":
        review = Reviews.objects.get(id=pk)
        review.delete()
        return redirect("/")
    
def reviews_update(request, pk):
    review = Reviews.objects.get(id=pk)

    if request.method == "POST":
        review.title = request.POST["title"]
        createdDate_str = request.POST["createdDate"]
        review.createdDate = datetime.fromisoformat(createdDate_str)
        review.genre = request.POST["genre"]
        review.rank = request.POST["rank"]
        running_time_str = request.POST["running_time"]
        hours, minutes, seconds = map(int, running_time_str.split(':'))
        review.running_time = time(hour=hours, minute=minutes, second=seconds)
        review.content = request.POST["content"]
        review.director = request.POST["director"]
        review.actors = request.POST["actors"]
        review.save()
        return redirect(f"/{pk}")
    
    context = {
        "review" : review   
    }
    return render(request, 'reviews_update.html', context)