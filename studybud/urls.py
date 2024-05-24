from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('signup/', views.signupView, name='signup'),
    path('update-user/', views.updateUserView, name='update-user'),
    path('room/<int:pk>', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<int:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<int:pk>/', views.deleteRoom, name='delete-room'),
    path('profile/<int:pk>/', views.userProfileView, name='profile'),
    path('delete-message/<int:pk>/', views.deleteMessage, name='delete-message'),
    path('topics/', views.topicsPageView, name='topics'),
    path('activity/', views.activityPageView, name='activity'),
]
