from django.urls import path
from .views import index

app_name = "weather"
urlpatterns = [
    path('', index, name="home")
]