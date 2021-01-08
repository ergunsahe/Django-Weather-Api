from django.urls import path
from .views import index, delete_city

app_name = "weather"
urlpatterns = [
    path('', index, name="home"),
    path('<int:id>/delete', delete_city, name="delete")
]