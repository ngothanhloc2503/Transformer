from django.urls import path
from . import views

urlpatterns = [
    path('data', views.get_data),
    path('summarize-text', views.summarize_text),
]