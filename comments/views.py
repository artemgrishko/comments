from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import CommentForm
from .models import Comment


class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'
    context_object_name = 'comments'
    paginate_by = 2

    def get_queryset(self):
        queryset = Comment.objects.filter(parent=None)
        sort_by = self.request.GET.get('sort_by')
        if sort_by in ['user_name', 'email', 'created_at']:
            order = self.request.GET.get('order', 'asc')
            if order == 'desc':
                sort_by = '-' + sort_by
            queryset = queryset.order_by(sort_by)
        return queryset


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'comments/create_comment.html', {'form': form})


def comment_detail(request, pk):
    parent_comment = Comment.objects.get(pk=pk)
    replies = parent_comment.replies.all()

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            new_comment = form.save(commit=False)
            new_comment.parent = parent_comment
            new_comment.save()
            return redirect('comment_detail', pk=pk)
    else:
        form = CommentForm(initial={'parent': parent_comment})
    return render(request, 'comments/comment_detail.html', {'parent_comment': parent_comment, 'replies': replies, 'form': form})
