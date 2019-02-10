from django.shortcuts import render, get_object_or_404, redirect
from .models import AgriculturePost
from .forms import AgriculturePostForm
from django_summernote import models as summer_model

# Create your views here.
def index(request):
    agricultureposts = AgriculturePost.objects.all
    return render(request, 'agriculture/index.html', {
        'posts':agricultureposts,
    })

def new(request):
    if request.method == 'POST':
        form = AgriculturePostForm(request.POST)
        if form.is_valid():
            agriculturepost = form.save(commit=False)     #이 부분은 아직도 모르겠다 ㅠ
            agriculturepost.save()
            return redirect('agriculture:index')
        else:
            return redirect('agriculture:new')
    else:
        form = AgriculturePostForm()
    return render(request, 'agriculture/new.html', {
        'form':form,
    })

def detail(request, post_id):
    post = get_object_or_404(AgriculturePost, pk=post_id)
    
    multiFile = get_object_or_404(summer_model.Attachment, id = post_id)
    return render(request, 'agriculture/detail.html', {
        'post':post,
        'multiFile':multiFile,
    })

def edit(request, post_id):
    post = get_object_or_404(AgriculturePost, pk=post_id)

    if request.method == 'POST':
        form = AgriculturePostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('agriculture:detail', post_id)
    else:
        form = AgriculturePostForm(instance=post)
    return render(request, 'agriculture/edit.html', {
        'form':form,
    })

def delete(request, post_id):
    post = get_object_or_404(AgriculturePost, pk=post_id)
    post.delete()
    return redirect('agriculture:index')
