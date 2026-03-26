from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Hashtag

from .forms import PostForm

def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

def detail(request, post_id):
    post_detail=get_object_or_404(Post, pk=post_id)
    post_hashtag=post_detail.hashtag.all()
    return render(request, 'detail.html', {'post': post_detail, 'hashing': post_hashtag})

def new(request):
    form=PostForm()
    return render(request, 'new.html', {'form':form})

def create (request):
    form=PostForm(request.POST, request.FILES)
    if form.is_valid():
        new_diary=form.save(commit=False)
        new_diary.save()
        hashtags=request.POST['hashtags']
        hashtag_list=hashtags.split(', ')

        for tag in hashtag_list:
            tag = tag.strip()
            new_hashtag=Hashtag.objects.get_or_create(hashtag=tag)
            new_diary.hashtag.add(new_hashtag[0])
        return redirect('diary:detail', new_diary.id)
    return redirect('diary:home')

def delete(request, post_id):
    delete_diary = get_object_or_404(Post, pk=post_id)
    delete_diary.delete()
    return redirect('diary:home')

def update_page(request, post_id):
    update_diary = get_object_or_404(Post, pk=post_id)
    return render(request, 'update.html', {'update_diary': update_diary})

def update_post(request, post_id):
    update_diary = get_object_or_404(Post, pk=post_id)
    update_diary.title = request.POST['title']
    update_diary.content = request.POST['content']
    update_diary.save()
    return redirect('diary:home')