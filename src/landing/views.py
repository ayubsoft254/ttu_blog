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

def stories(request):
    return render(request, 'stories.html')

def opinion(request):
    return render(request, 'opinion.html')

def open_relationships_101(request):
    return render(request, 'open_relationships_101.html')

def tag_stories(request):
    return render(request, 'tag_stories.html')

def author_stamos(request):
    return render(request, 'author_stamos.html')

def author_ilya(request):
    return render(request, 'author_ilya.html')

def author_menenaba(request):
    return render(request, 'author_menenaba.html')

def author_anonymous(request):
    return render(request, 'author_anonymous.html')

def author_questionmike(request):
    return render(request, 'author_questionmike.html')
