from django.urls import path
from . import views

urlpatterns = [
    path('ragada_app', views.ragada_app, name='ragada_app'),
]