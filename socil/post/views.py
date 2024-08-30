from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from post.forms import PostForm
from post.models import Post


class PostView(LoginRequiredMixin, View):
    template_name = 'posts.html'

    def get(self, request):
        posts = Post.objects.filter(author=request.user)
        context = {
            "posts": posts,
        }
        return render(request, self.template_name,  context=context)


class PostDetailView(LoginRequiredMixin, View):
    template_name = 'post_detail.html'

    def get(self, request, post_pk):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return redirect('posts')

        form = PostForm(instance=post)
        context = {
            "post": post,
            "form": form,
        }
        return render(request, self.template_name,  context=context)


class PostCreateView(LoginRequiredMixin, View):
    template_name = 'create_post.html'

    def get(self, request):
        form = PostForm()
        context = {
            "form": form,
        }
        return render(request, self.template_name,  context=context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')

        context = {
            "form": form,
        }
        return render(request, self.template_name,  context=context)

