from django.shortcuts import render, get_object_or_404, redirect
from .models import BusinessPost,BusinessComment
from .forms import BusinessPostForm,BusinessAdminPostForm,BusinessCommentForm
from django_summernote import models as summer_model
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from account.models import CustomUser
from notify.signals import notify

def index(request):
    businessposts = BusinessPost.objects.all
    notices = BusinessPost.objects.filter(notice=True)

    return render(request, 'business/index.html', {
        'posts':businessposts,
        'notices':notices,
    })

@login_required
def new(request):
    current_user = request.user

    if request.method == 'POST':
        if current_user.is_superuser:
            form = BusinessAdminPostForm(request.POST)
        else:
            form = BusinessPostForm(request.POST)

        if form.is_valid():
            businesspost = form.save(commit=False)     #이 부분은 아직도 모르겠다 ㅠ
            businesspost.user = current_user
            businesspost.save()
            return redirect('business:index')
        else:
            return redirect('business:new')

    else:
        if current_user.is_superuser:
            form = BusinessAdminPostForm()
        else:
            form = BusinessPostForm()

    return render(request, 'business/new.html', {
        'form':form,
    })

def detail(request, post_id):
    post = get_object_or_404(BusinessPost, pk=post_id)
    form = BusinessCommentForm()
    comments = post.comments
    firstcomments = BusinessComment.objects.filter(depth=0, post=post.id)
    secondcomments = BusinessComment.objects.filter(depth=1, post=post.id)
    
    # multiFile = get_object_or_404(summer_model.Attachment, id = post_id) #오류로 인한 제외
    return render(request, 'business/detail.html', {
        'post':post,
        'form':form,
        'firstcomments':firstcomments,
        'secondcomments':secondcomments,
        # 'multiFile':multiFile, #오류로 인한 제외
    })


@login_required
def edit(request, post_id):
    post = get_object_or_404(BusinessPost, pk=post_id)
    current_user = request.user

    if request.method == 'POST':
        if current_user.is_superuser:
            form = BusinessAdminPostForm(request.POST, instance=post)
        else:
            form = BusinessPostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.updated_at = timezone.datetime.now()
            post.save()
            return redirect('business:detail', post_id)

    else:
        if current_user.is_superuser:
            form = BusinessAdminPostForm(instance=post)
        else:
            form = BusinessPostForm(instance=post)
            
    return render(request, 'business/edit.html', {
        'form':form,
    })

@login_required
def delete(request, post_id):
    post = get_object_or_404(BusinessPost, pk=post_id)
    post.delete()
    return redirect('business:index')


@login_required
def add_comment_to_post(request, post_id):
    post = get_object_or_404(BusinessPost, pk=post_id)
    user = post.user 

    if request.method == 'POST':
        form = BusinessCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user.username
            comment.save()

            if request.user != user:
                notify.send(request.user, recipient=user, actor=request.user, description='business',
                    verb='add comment your post : '+post.title, target=post, nf_type='add_comment')

            return redirect('business:detail', post.id)

@login_required
def add_comment_to_comment(request, comment_id):
    comment = get_object_or_404(BusinessComment, pk=comment_id)
    post = comment.post
    user = post.user
    if request.method =='POST':
        form = BusinessCommentForm(request.POST)
        if form.is_valid():
            recomment = form.save(commit=False)
            recomment.post = post
            recomment.parent = comment.id
            recomment.depth = 1
            recomment.user = request.user.username
            recomment.save()

            if request.user != user:
                notify.send(request.user, recipient=user, actor=request.user, description='business',
                    verb='add recomment your comment : '+post.title, target=post, nf_type='add_comment')

            return redirect('business:detail', post.id)

@login_required
def remove_comment(request, post_id, comment_id):
    comment = get_object_or_404(BusinessComment, pk=comment_id)
    if comment.parent: 
        comment.delete()
    else: 
        comment.text = '삭제된 댓글입니다'
        comment.save()
    return redirect('business:detail', post_id)