from django.shortcuts import render, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark  # bookmark_list -> HTML(bookmark_list.html)


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name', 'url']  # '__all__'
    template_name_suffix = '_create'  # 원래는 '_form' -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['name', 'url']           #'__all__'
    template_name_suffix = '_update'   #원래는 '_form' -> bookmark_update.html
    success_url = reverse_lazy('bookmark:list')












