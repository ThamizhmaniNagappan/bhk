from django.urls import path  # type: ignore[import]
from .views import home

urlpatterns = [
    path('', home, name='home')
]