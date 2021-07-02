from django.urls import path, include
from menu.views import menu

urlpatterns = [
    path('',menu.home, name="menu_home"),
    path('add/',menu.add, name="menu_add"),
    path('edit/<int:id>/',menu.edit, name="menu_edit"),
    path('delete/<int:id>',menu.delete, name="menu_delete"),
    path('<uuid:uuid>',menu.options, name="menu_options"),
    path('send/<int:id>',menu.send, name="menu_send"),
    path('', include('menu.urls.option')),
]
