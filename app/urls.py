from django.urls import path
from .views import home, alojamientos, servicios

urlpatterns = [
    path('', home, name="home"),
    path('alojamientos/', alojamientos, name="alojamientos"),
    path('servicios/', servicios, name="servicios"),
]
