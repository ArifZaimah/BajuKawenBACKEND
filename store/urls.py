from django.urls import path
from . import views

urlpatterns = [
    path("users/list/", views.get_user_list, name="get_user_list"),
    path('users/create/', views.create_user, name='create_user'),
]
