from django.shortcuts import render
from .models import Opinion, Story

def opinion(request):
    opinions = Opinion.objects.all().order_by('-date_posted')[:6]
    context = {
        'opinions': opinions
    }
    return render(request, 'opinions.html', context)

def story(request):
    stories = Story.objects.all().order_by('-date_posted')[:6]
    context = {
        'stories': stories
    }
    return render(request, 'stories.html', context)
