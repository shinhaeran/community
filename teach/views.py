from django.shortcuts import render, get_object_or_404, redirect
from .models import TeachPost, TeachComment
from .forms import TeachPostForm, TeachAdminPostForm, TeachCommentForm
from django_summernote import models as summer_model
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from account.models import CustomUser
from notify.signals import notify
# Create your views here.
def index(request):
    teachposts = TeachPost.objects.all
    notices = TeachPost.objects.filter(notice=True)

    return render(request, 'teach/index.html', {
        'posts':teachposts,
        'notices':notices,
    })

@login_required
def new(request):
    current_user = request.user

    if request.method == 'POST':
        if current_user.is_superuser:
            form = TeachAdminPostForm(request.POST)
        else:
            form = TeachPostForm(request.POST)

        if form.is_valid():
            teachpost = form.save(commit=False)
            teachpost.user = current_user     #이 부분은 아직도 모르겠다 ㅠ
            teachpost.save()
            return redirect('teach:index')
        else:
            return redirect('teach:new')

    else:
        if current_user.is_superuser:
            form = TeachAdminPostForm()
        else:
            form = TeachPostForm()

    return render(request, 'teach/new.html', {
        'form':form,
    })

def detail(request, post_id):
    post = get_object_or_404(TeachPost, pk=post_id)
    form = TeachCommentForm()
    comments = post.comments
    firstcomments = TeachComment.objects.filter(depth=0, post=post.id)
    secondcomments = TeachComment.objects.filter(depth=1, post=post.id)
    
    # multiFile = get_object_or_404(summer_model.Attachment, id = post_id) #오류로 인한 제외
    return render(request, 'teach/detail.html', {
        'post':post,
        'form':form,
        'firstcomments':firstcomments,
        'secondcomments':secondcomments,
        # 'multiFile':multiFile, #오류로 인한 제외
    })

@login_required
def edit(request, post_id):
    post = get_object_or_404(TeachPost, pk=post_id)
    current_user = request.user

    if request.method == 'POST':
        if current_user.is_superuser:
            form = TeachAdminPostForm(request.POST, instance=post)
        else:
            form = TeachPostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.updated_at = timezone.datetime.now()
            post.save()
            return redirect('teach:detail', post_id)

    else:
        if current_user.is_superuser:
            form = TeachAdminPostForm(instance=post)
        else:
            form = TeachPostForm(instance=post)
            
    return render(request, 'teach/edit.html', {
        'form':form,
    })

@login_required
def delete(request, post_id):
    post = get_object_or_404(TeachPost, pk=post_id)
    post.delete()
    return redirect('teach:index')


@login_required
def add_comment_to_post(request, post_id):
    post = get_object_or_404(TeachPost, pk=post_id)
    user = post.user 
    if request.method == 'POST':
        form = TeachCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user.username
            comment.save()
            
            if request.user != user:
                notify.send(request.user, recipient=user, actor=request.user, description='teach',
                    verb='add comment your post : '+post.title, target=post, nf_type='add_comment')

            return redirect('teach:detail', post.id)

@login_required
def add_comment_to_comment(request, comment_id):
    comment = get_object_or_404(TeachComment, pk=comment_id)
    post = comment.post
    user = post.user
    if request.method =='POST':
        form = TeachCommentForm(request.POST)
        if form.is_valid():
            recomment = form.save(commit=False)
            recomment.post = post
            recomment.parent = comment.id
            recomment.depth = 1
            recomment.user = request.user.username
            recomment.save()
            
            if request.user != user:
                notify.send(request.user, recipient=user, actor=request.user, description='teach',
                    verb='add recomment your comment : '+post.title, target=post, nf_type='add_comment')

            return redirect('teach:detail', post.id)


@login_required
def remove_comment(request, post_id, comment_id):
    comment = get_object_or_404(TeachComment, pk=comment_id)
    if comment.parent: 
        comment.delete()
    else: 
        comment.text = '삭제된 댓글입니다'
        comment.save()
    return redirect('business:detail', post_id)