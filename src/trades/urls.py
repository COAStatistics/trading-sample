from django.urls import path
from .views import trade, sample

urlpatterns = [
    path('', trade, name='trade'),
    path('sample/', sample, name='sample'),
]
