from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark  # bookmark_list -> HTML(bookmark_list.html)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            bookmark_list = Bookmark.objects.filter(user=user)
        else:
            bookmark_list = Bookmark.objects.all()
        return bookmark_list


class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['user', 'name', 'url']  # '__all__'
    template_name_suffix = '_create'  # 원래는 '_form' -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')

    def get_initial(self):
        user = self.request.user
        return {'user': user}


class BookmarkDetailView(LoginRequiredMixin, DetailView):
    model = Bookmark


class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['name', 'url']  # '__all__'
    template_name_suffix = '_update'  # 원래는 '_form' -> bookmark_update.html
    success_url = reverse_lazy('bookmark:list')


class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')
