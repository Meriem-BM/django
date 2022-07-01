from re import split
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views import generic
from django.urls import reverse
from .models import Post
from .forms import PostForm

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'slug', 'author', 'content', 'status', 'image']
    template_name = 'create_post.html'
    def get_success_url(self):
        post = Post.objects.get(slug=self.object.slug)
        print(post.content.name)
        name_splited = []
        name_splited = post.content.name.split('/')
        post.content.name = ''
        for i in range(1, len(name_splited)):
            post.content.name += name_splited[i] + '/'
        print(post.content.name)
        print(len(name_splited))
        post.content.name = post.content.name[:-1]
        print(post.content.name)
        post.save()
        return reverse('post_detail', kwargs={'slug': self.object.slug})

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'