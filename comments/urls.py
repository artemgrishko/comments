from django.urls import path

from . import views
from .views import CommentListView

urlpatterns = [
    path('', CommentListView.as_view(), name='comment_list'),
    path('create/', views.create_comment, name='create_comment'),
]