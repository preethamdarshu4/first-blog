
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
    path('auth/users/login/', auth_views.LoginView.as_view(template_name='blog/registration/login.html'), name='login'),
    path('auth/user/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('auth/user/settings/password_change/', auth_views.PasswordChangeView.as_view(template_name='blog/password_change.html'), name='password_change'),
    path('auth/user/settings/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='blog/password_change_done.html'), name='password_change_done'),
    path('user/account/', views.user_account, name='user_account')
]

