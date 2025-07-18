# listings/urls.py

from django.urls import path
from .views import SampleView  # or any view you've created

urlpatterns = [
    path('sample/', SampleView.as_view(), name='sample'),  # test endpoint
]
