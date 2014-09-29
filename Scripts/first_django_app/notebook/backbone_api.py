import backbone

from notebook.models import NotebookRow


class NotebookRowAPIView(backbone.views.BackboneAPIView):
    model = NotebookRow
    display_fields = ('description', 'status')


backbone.site.register(NotebookRowAPIView)
