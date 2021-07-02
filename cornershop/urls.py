from django.urls import path, include

urlpatterns = [
    path('', include('menu.urls.access')),
    path('menu/', include('menu.urls.menu')),
    path('food/', include('menu.urls.food')),
    path('orders/', include('menu.urls.order')),
]
