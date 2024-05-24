from django.urls import path
from studybud.api import views


urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<int:pk>/', views.getRoom),

]
