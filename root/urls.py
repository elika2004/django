from django.urls import path
from .views import home,contactus,aboutus


urlpatterns = [
    path('',home),
    path('contactus',contactus),
    path('aboutus',aboutus),
]
