from django.contrib import admin
<<<<<<< HEAD
from .models import Story, Opinion
from .models import Category, Tag, Story, Comment, Opinion, Like

# Register your models here.
=======
from .models import Story, Comment, Opinion, Like

# Register your models here.

>>>>>>> d6968ac (Modified Story model to include comments and likes relationships and defined the views and form)
admin.site.register(Story)
admin.site.register(Opinion)
admin.site.register(Like)
