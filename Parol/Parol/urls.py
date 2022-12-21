
from django.urls import path
from generator import views

urlpatterns = [
    path('', views.home, name='home'),
    path('password', views.password, name="pass"),
    path('info', views.infor, name="in")
]
