from django.urls import path
from . import views

#name represents the identifier for this view. whereas views.post_list is the name of the view file to be rendered.

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('py', views.py, name='py'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]