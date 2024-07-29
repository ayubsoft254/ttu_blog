<<<<<<< HEAD
from django.shortcuts import render
from .models import Opinion, Story
=======
from django.shortcuts import render, redirect
from .models import Opinion, Story, Comment, Like
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
>>>>>>> d6968ac (Modified Story model to include comments and likes relationships and defined the views and form)

def opinion(request):
    opinions = Opinion.objects.all().order_by('-date_posted')[:6]
    context = {
        'opinions': opinions
    }
    return render(request, 'opinions.html', context)

def story(request):
    stories = Story.objects.all().order_by('-created_at')[:6]
    context = {
        'stories': stories
    }
    return render(request, 'stories.html', context)
<<<<<<< HEAD
=======

def story_detail(request, pk):
    story = Story.objects.get(pk=pk)
    comments = story.comments.all()
    comment_form = CommentForm()

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.author = request.user
                new_comment.story = story
                new_comment.save()
                return redirect('story_detail', pk=story.pk)
        elif 'like_submit' in request.POST:
            if request.user.is_authenticated:
                like, created = Like.objects.get_or_create(author=request.user, story=story)
                if not created:
                    like.delete()
                return redirect('story_detail', pk=story.pk)

    liked = story.likes.filter(author=request.user).exists()

    context = {
        'story': story,
        'comments': comments,
        'comment_form': comment_form,
        'liked': liked,
    }
    return render(request, 'story_detail.html', context)
>>>>>>> d6968ac (Modified Story model to include comments and likes relationships and defined the views and form)
