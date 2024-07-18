from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def write_story(request):
    return render(request, 'write_story.html')
