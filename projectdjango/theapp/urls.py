from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('edit-post/<int:pk>', views.editPost, name="edit_post"),
]