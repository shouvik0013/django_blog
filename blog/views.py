from django.shortcuts import render
from django.views.generic import ListView, DetailView


from .models import Post


class BlogListView(ListView):
    model           = Post
    template_name   = 'home.html'



class BlogDetailView(DetailView):
    model           = Post
    template_name   = 'post_detail.html'
    # if we want to change the context object name then nxt line is the answer
    # context_object_name = 'anything'
    