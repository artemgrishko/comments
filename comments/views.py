from django.views.generic import ListView

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
