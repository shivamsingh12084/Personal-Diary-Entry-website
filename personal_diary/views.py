
from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from django.views.generic.edit import UpdateView
from . models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class TitleListView(ListView):
    model = Post
    context_object_name = 'title_list'
    template_name = "personal_diary/title_list.html"
    ordering = ['-date_posted']


class TitleDetailView(DetailView):
    model = Post
    template_name = "personal_diary/title_detail.html"
    context_object_name = 'title_detail'


class TitleCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "personal_diary/title_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TitleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "personal_diary/title_update.html"

    def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TitleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "personal_diary/title_delete.html"
    success_url = "/personal_diary/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    