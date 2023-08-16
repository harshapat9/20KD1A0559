from django.urls import path,include
from . import views

urlpatterns = [
    path('number',views.number, name="number")
]
