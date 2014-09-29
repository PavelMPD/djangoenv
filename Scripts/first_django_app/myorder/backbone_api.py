import backbone

from myorder.models import MyOrder


class OrderAPIView(backbone.views.BackboneAPIView):
    model = MyOrder
    display_fields = ('name', 'description')


backbone.site.register(OrderAPIView)