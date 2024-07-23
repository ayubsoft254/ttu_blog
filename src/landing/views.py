from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def write_story(request):
    return render(request, 'write_story.html')

def k_pop_queerbating(request):
    return render(request, 'k_pop_queerbating.html')

def open_relationships(request):
    return render(request, 'open_relationships.html')

def story(request):
    return render(request, 'story.html')

def opinion(request):
    return render(request, 'opinion.html')

