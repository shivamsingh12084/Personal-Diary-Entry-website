from django.urls import path
from . views import HomePageView, MainView


urlpatterns = [
    path('', HomePageView.as_view(), name='home' ),
    path('main/', MainView.as_view(), name='main'),
    
]