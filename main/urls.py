from django.urls import path
from .views import *

urlpatterns = [
    path('', add_url, name='add_url'),
    path('short_code/<str:short_code>/', short_code_page, name='short_code'),
    path('<str:short_code>/', redirect_to_original, name='redirect_to_original'),
]
