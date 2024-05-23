from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('record/<int:pk>/', views.record_detail, name='record_detail'),
    path('record/new/', views.record_new, name='record_new'),
    path('record/<int:pk>/edit/', views.record_edit, name='record_edit'),
]
