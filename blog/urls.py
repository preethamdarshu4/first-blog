
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('drafts/post/<int:pk>/', views.post_details, name='draft_post_details'), 
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('drafts/post/<int:pk>/edit/', views.edit_post, name='drafts_edit_post'),
    path('drafts/', views.draft_post_list, name='draft_post_list'),
    path('drafts/post/<int:pk>/publish/', views.publish_post, name='publish_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('drafts/post/<int:pk>/delete/', views.delete_post, name='drafts_delete_post'),
    path('auth/users/signup/', views.signup, name="signup"),
    path('auth/users/login/', auth_views.LoginView.as_view(), name='login'),
    path('auth/users/logout/', auth_views.LogoutView.as_view(), name='logout'),
]

