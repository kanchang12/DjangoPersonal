from django.urls import path
from .views import HomePageView
from .views import index

urlpatterns =[

    path('', HomePageView, name='index'),
    path('', index, name='index'),
]