
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('drafts/', views.draft_post_list, name='draft_post_list'),
    path('post/<int:pk>/publish/', views.publish_post, name='publish_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
]

