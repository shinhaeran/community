from django.shortcuts import render, get_object_or_404, redirect
from .models import HumanPost
from .forms import HumanPostForm
from django_summernote import models as summer_model
# Create your views here.

def index(request):
   humanposts = HumanPost.objects.all
   return render(request, 'human/index.html', {
        'posts':humanposts,
    })

def new(request):
    if request.method == 'POST':
        form = HumanPostForm(request.POST)
        if form.is_valid():
            humanpost = form.save(commit=False)     #이 부분은 아직도 모르겠다 ㅠ
            humanpost.save()
            return redirect('human:index')
        else:
            return redirect('human:new')
    else:
        form = HumanPostForm()
    return render(request, 'human/new.html', {
        'form':form,
    })

def detail(request, post_id):
    post = get_object_or_404(HumanPost, pk=post_id)
    multiFile = get_object_or_404(summer_model.Attachment, id = post_id)
    return render(request, 'human/detail.html', {
        'post':post,
        'multiFile':multiFile,
    })

def edit(request, post_id):
    post = get_object_or_404(HumanPost, pk=post_id)

    if request.method == 'POST':
        form = HumanPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('human:detail', post_id)
    else:
        form = HumanPostForm(instance=post)
    return render(request, 'human/edit.html', {
        'form':form,
    })

def delete(request, post_id):
    post = get_object_or_404(HumanPost, pk=post_id)
    post.delete()
    return redirect('human:index')
