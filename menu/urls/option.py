from django.urls import path
from menu.views import option

urlpatterns = [
    path('options/<int:menu_id>',option.home, name="option_home"),
    path('options/add/<int:menu_id>',option.add, name="option_add"),
    path('option/edit/<int:id>/',option.edit, name="option_edit"),
    path('option/delete/<int:id>',option.delete, name="option_delete")
]
