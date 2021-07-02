from django.urls import path, include
from menu.views import order

urlpatterns = [
    path('',order.home, name="order_home"),
    path('edit/<int:id>/',order.edit, name="order_edit"),
    path('delete/<int:id>/',order.delete, name="order_delete"),
    path('view/<int:id>/',order.view, name="order_view"),
]