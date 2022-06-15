from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, SignupForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/post_list.html', {'posts': posts, 'type': 'Published Posts'})


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.published_date and post.created_date:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post_id = post
                comment.author = request.user
                comment.save()
                return redirect('post_details', pk=post.pk)
        else:
            form = CommentForm()
        return render(request, 'blog/post_details.html', {'post': post, 'type1': 'Published Posts', 'type2': 'Post: ' + str(pk), 'form': form})
    else:
        return render(request, 'blog/post_details.html', {'post': post, 'type1': 'Drafts', 'type2': 'Post: ' + str(pk)})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'blog/registration/signup.html', {'form': form, 'type': 'Signup'})

@login_required(login_url='login')
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_details', pk=post.pk)
    else:    
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form':form, 'type1': 'Posts','type2':'New post'})


@login_required(login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/new_post.html', {'form': form, 'type':'Edit post'})

@login_required(login_url='login')
def draft_post_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/draft_post_list.html', {'posts': posts, 'type1': 'Posts', 'type2':'Drafts '})

@login_required(login_url='login')
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_details', pk=pk)

@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required(login_url='login')
def user_account(request):
    user = get_object_or_404(User, username=request.user)
    return render(request, 'blog/user_account.html', {'user': user, 'type1': 'My account'})
