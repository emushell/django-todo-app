from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('', views.index, name='index'),

    path('create-task/', views.create_task, name='create_task'),
    path('update-task/<int:task_id>/', views.update_task, name='update_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),

    path('profile/', views.profile, name='profile'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="todo/password_reset.html"),
         name="reset_password"),
    path('password-reset-sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="todo/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="todo/password_reset_form.html"),
         name="password_reset_confirm"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="todo/password_reset_done.html"),
         name="password_reset_complete"),
]
