from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    if request.method == "POST":
        if "submit_post" in request.POST:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.posted_at = timezone.now()
                post.save()
                return redirect('index')
        elif "delete_post" in request.POST:
            return destroyPost(pk = request.POST.get('post_pk', 'Default'))
    else:
        form = PostForm()
        posts = Post.objects.filter(posted_at__lte=timezone.now()).order_by('-posted_at')

    return render(request, 'index.html', {'posts' : posts, 'form' : form})

def editPost(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_at = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm(instance=post)
        posts = Post.objects.filter(posted_at__lte=timezone.now()).order_by('-posted_at')

    return render(request, 'index.html', {'form' : form}) 
    
def destroyPost(pk):
    post = Post.objects.get(id = pk)
    post.delete()
    return redirect('index')