from django.shortcuts import render
from blog.models import Post
from django.utils import timezone as tz

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=tz.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})