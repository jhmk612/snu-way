from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib.auth.models import User
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

@login_required
def lend_list(request):
    lend_list = Post.objects.all()
    context = {
        "lend_list": lend_list,

    }
    return render(request, 'blog/lend_list.html', context)

@login_required
def lend_detail(request, lend_id):
    instance = get_object_or_404(Post, pk=lend_id)
    context = {
        "instance":instance,
    }
    return render(request, 'blog/lend_detail.html', context)

# form 사용
@login_required
def lend(request):
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("blog:lend_list")
    else:
        form = PostForm()

    return render(request, 'blog/lend.html', {
        "form": form,
        })

def my_page(request, user_id):
    user = User.objects.get(pk=user_id)
    user_posts = Post.objects.filter(author=user_id)
    context = {
    "user":user,
    "user_posts":user_posts,
    }
    return render(request, "blog/my.html", context)

