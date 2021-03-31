from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like
from profiles.models import UserProfile
from .forms import PostForm, CommentForm, LikeForm

from django.contrib import messages


def view_posts(request):
    """ View to show all posts, comment and like counts page """
    template = 'community/view_posts.html'
    posts = Post.objects.all()
    comments = Comment.objects.all()
    likes = Like.objects.all()

    try:
        user = get_object_or_404(UserProfile, user=request.user)
    except Exception:
        user = "AnonymousUser"
        messages.info(request, 'You need to log in to add comments/posts.')

    for post in posts:
        post.likes = Like.objects.filter(post=post.id).count()
        post.comments = Comment.objects.filter(for_post=post.id).count

    # Search posts by search query
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any \
                                         search criteria!")
                return redirect(reverse('view_posts'))
            queries = Q(heading__icontains=query) | Q(body__icontains=query)
            posts = posts.filter(queries)
            for post in posts:
                post.likes = Like.objects.filter(post=post.id).count()
                post.comments = Comment.objects.filter(for_post=post.id).count

    context = {
        'posts': posts,
        'comments': comments,
        'user': user,
        'likes': likes,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    """ View to show full post, comments and likes """
    try:
        user = get_object_or_404(UserProfile, user=request.user)
    except Exception:
        user = 'AnonymousUser'
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(for_post=post)
    likes = Like.objects.filter(post=post_id)
    like_count = likes.count()
    comment_count = comments.count()

    # Add comment form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment Added!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, "Comment couldn't be added. Please check over \
                           your form.")
    else:
        form = CommentForm()

    template = 'community/post_detail.html'
    context = {
        'post': post,
        'comments': comments,
        'user': user,
        'like_count': like_count,
        'comment_count': comment_count,
    }
    return render(request, template, context)


@login_required
def like(request, post_id):
    """ View to add/remove like from a post """
    if request.method == 'POST':
        form = LikeForm(request.POST)
        user = get_object_or_404(UserProfile, user=request.user)
        post = get_object_or_404(Post, id=post_id)
        if form.is_valid():
            liked = Like.objects.filter(user=user, post=post).exists()
            if liked:
                liked = Like.objects.filter(user=user, post=post)
                liked.delete()
                messages.success(request, "Unliked!")
                return redirect(reverse('post_detail', args=[post.id]))
            else:
                form.save()
                messages.success(request, 'Liked!')
                return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, "Something went wrong. Please try again \
                           later")
            return redirect(reverse('post_detail', args=[post.id]))
    else:
        form = LikeForm()


@login_required
def add_post(request):
    """ View to add a post """
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Added!')
            return redirect(reverse('view_posts'))
        else:
            messages.error(request, "Post couldn't be added. Please check \
                           over your form.")
    else:
        form = PostForm()
    template = 'community/add_post.html'
    context = {
        'form': form,
        'user': user,
    }
    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """ View to edit post """
    user = get_object_or_404(UserProfile, user=request.user)
    post = get_object_or_404(Post, id=post_id)
    if user != post.user_profile:
        messages.error(request, 'Sorry, you can only edit your own posts.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated!")
            return redirect(reverse('view_posts'))
        else:
            messages.error(request, 'Post update failed. Please check form is \
                           valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.heading}')

    template = 'community/edit_post.html'
    context = {
        'form': form,
        'post': post,
        'user': user,
    }
    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    """ View to delete a comment  """
    user = get_object_or_404(UserProfile, user=request.user)
    comment = get_object_or_404(Comment, id=comment_id)
    post = comment.for_post
    if user == comment.user_profile or user.user.is_superuser:
        comment.delete()
        messages.success(request, 'Comment Deleted!')
        return redirect(reverse('post_detail', args=[post.id]))
    else:
        messages.error(request, 'Sorry, you can only delete your own \
                       comments.')
    return redirect(reverse('view_posts'))


@login_required
def delete_post(request, post_id):
    """ View to delete a post """
    user = get_object_or_404(UserProfile, user=request.user)
    post = get_object_or_404(Post, id=post_id)
    if user == post.user_profile:
        post.delete()
        messages.success(request, 'Post Deleted!')
    elif user.user.is_superuser:
        post.delete()
        messages.success(request, 'Post Deleted!')
    else:
        messages.error(request, 'Sorry, you can only delete your own posts.')
    return redirect(reverse('view_posts'))


@login_required
def edit_comment(request, comment_id):
    """ View to edit a comment """
    user = get_object_or_404(UserProfile, user=request.user)
    comment = get_object_or_404(Comment, id=comment_id)
    post = comment.for_post
    if user != comment.user_profile:
        messages.error(request, 'Sorry, you can only edit your own comments.')
        return redirect(reverse('view_posts'))

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated!")
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Comment update failed. Please check form \
                           is valid.')
            return redirect(reverse('post_detail', args=[post.id]))
    else:
        form = CommentForm(instance=comment)
        messages.info(request, f'You are editing {comment.body}')
