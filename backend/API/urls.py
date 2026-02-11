from django.urls import path
from .views import test_protected

urlpatterns = [
    path('protected/', test_protected),
]
