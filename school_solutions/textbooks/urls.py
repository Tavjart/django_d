from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:grade>/<str:subject>/', views.textbook_list, name='textbook_list'),
    path('<str:grade>/<str:subject>/<str:short_name>/', views.textbook_detail, name='textbook_detail'),
    path('<int:grade>/<str:subject>/<str:short_name>/<str:folder>/<str:image_name>/', views.solution_detail, name='solution_detail'),
]
