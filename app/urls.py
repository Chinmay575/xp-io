from django.urls import path
from . import views

urlpatterns = [
    path('get-extracted-data/', views.get_data, name='app'),
]