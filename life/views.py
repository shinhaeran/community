from django.shortcuts import render, get_object_or_404, redirect
from .models import LifePost
from .forms import LifePostForm
from django_summernote import models as summer_model
# Create your views here.

def index(request):
    lifeposts = LifePost.objects.all
    return render(request, 'life/index.html', {
        'posts':lifeposts,
    })
#ㅠ
def new(request):
    if request.method == 'POST':
        form = LifePostForm(request.POST)
        if form.is_valid():
            lifepost = form.save(commit=False)     #이 부분은 아직도 모르겠다 ㅠ
            lifepost.save()
            return redirect('life:index')
        else:
            return redirect('life:new')
    else:
        form = LifePostForm()
    return render(request, 'life/new.html', {
        'form':form,
    })

def detail(request, post_id):
    post = get_object_or_404(LifePost, pk=post_id)
    multiFile = get_object_or_404(summer_model.Attachment, id = post_id)
    return render(request, 'life/detail.html', {
        'post':post,
        'multiFile':multiFile,
    })

def edit(request, post_id):
    post = get_object_or_404(LifePost, pk=post_id)

    if request.method == 'POST':
        form = LifePostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('life:detail', post_id)
    else:
        form = LifePostForm(instance=post)
    return render(request, 'life/edit.html', {
        'form':form,
    })

def delete(request, post_id):
    post = get_object_or_404(LifePost, pk=post_id)
    post.delete()
    return redirect('life:index')
