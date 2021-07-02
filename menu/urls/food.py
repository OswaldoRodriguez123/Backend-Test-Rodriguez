from django.urls import path
from menu.views import food

urlpatterns = [
    path('',food.home, name="food_home"),
    path('add/',food.add, name="food_add"),
    path('edit/<int:id>/',food.edit, name="food_edit"),
    path('delete/<int:id>',food.delete, name="food_delete")
]
