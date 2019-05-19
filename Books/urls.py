from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booklist/', views.booklist, name='booklist'),
    path('importbook/', views.importbook, name='importbook'),
    path('newbook/', views.newbook, name='newbook'),
    path('api_request/', views.api_request, name='api_request'),
]