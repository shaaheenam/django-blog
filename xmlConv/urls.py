from django.urls import path
from . import views
from .views import XMLtoTable

urlpatterns = [
    path('', XMLtoTable.as_view(), name='xmltopdf')
]