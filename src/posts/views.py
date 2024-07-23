from django.shortcuts import render

# Create your views here.
def opinion(request):
    return render(request, 'opinions.html')

def story(request):
    return render(request, 'stories.html')

