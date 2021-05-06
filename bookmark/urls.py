from django.urls import path

from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),  # {% url 'bookmark:list' %}
    path('add/', BookmarkCreateView.as_view(), name='add'), # {% url 'bookmark:add' %}
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'), # {% url 'bookmark:detail' pk=bookmark.pk %}
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'), # {% url 'bookmark:update' pk=bookmark.pk %}
]