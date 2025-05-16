from django.shortcuts import render, redirect
from .models import Film

def home(request):
    return render(request, 'index.html')

def feedback(request):
    films = Film.objects.all()
    return render(request, 'films/feedback.html', {'films': films})

def new_feedback(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        review = request.POST.get('review')
        Film.objects.create(title=title, description=description, review=review)
        return redirect('feedback')
    return render(request, 'films/new_feedback.html')