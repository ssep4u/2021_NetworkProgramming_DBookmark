from django.shortcuts import render
from django.views.generic import ListView

from .models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark    # bookmark_list -> HTML(bookmark_list.html)
