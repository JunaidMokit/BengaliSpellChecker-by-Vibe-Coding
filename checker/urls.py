from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/check/', views.check_text, name='check_text'),
]
