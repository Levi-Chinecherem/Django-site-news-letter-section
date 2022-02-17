
from django.urls import path
from .views import news_letter_view

urlpatterns = [
    path('news_letter/', news_letter_view, name='news_letter_view'),
]
