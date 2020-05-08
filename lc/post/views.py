from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect


class PostList(LoginRequiredMixin, ListView):
    login_url = 'accounts:login'
    template_name = 'post/all_posts.html'
    model= Post
    context_object_name = 'all'

    def get_queryset(self):
        return Post.objects.raw('SELECT * FROM post_post ORDER BY created_at DESC')



class PostDetail( LoginRequiredMixin , DetailView ):
    login_url= 'accounts:login'
    model = Post



class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = 'accounts:login'
    redirect_field_name = 'post/post_detail.html'
    form_class= PostForm
    model = Post



class UpdatePostView(LoginRequiredMixin , UpdateView):
    login_url = 'accounts:login'
    redirect_field_name = 'post/post_detail.html'
    form_class = PostForm
    model = Post


class DeletePostView(LoginRequiredMixin,  DeleteView):
    model = Post
    success_url = reverse_lazy('post:post_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post,  pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'post/comment_form.html', {'form':form})




@login_required
def comment_remove(request,  pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post:post_detail', pk=post_pk)



















