
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
    reply = mdl.ForeignKey('self', on_delete=mdl.CASCADE, blank=True, null=True, related_name='replies')
    text = mdl.TextField()
    created_date = mdl.DateTimeField(default=timezone.now)
    replying_to = mdl.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        format_option = str('commment num {}'.format(self.reply.pk)) if self.reply else str('post {}'.format(self.post_id.pk))
        return '(Num {}) Comment by {} on {}'.format(self.pk, self.author.username, format_option)
