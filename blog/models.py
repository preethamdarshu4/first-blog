from tkinter import CASCADE
from django.db import models as mdl
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(mdl.Model):
    author = mdl.ForeignKey(settings.AUTH_USER_MODEL, on_delete=mdl.CASCADE)
    title = mdl.CharField(max_length=200)
    text = mdl.TextField()
    created_date = mdl.DateTimeField(default=timezone.now)
    published_date = mdl.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Comment(mdl.Model):
    post_id = mdl.ForeignKey('blog.Post', on_delete=mdl.CASCADE, related_name='comments')
    author = mdl.ForeignKey(settings.AUTH_USER_MODEL, on_delete=mdl.CASCADE)
    text = mdl.TextField()
    created_date = mdl.DateTimeField(default=timezone.now)


    def approve_comment(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return 'Comment by: ' + self.author.username + ' on post ' + str(self.post_id.pk)