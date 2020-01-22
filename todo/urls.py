from django.urls import path
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
]
