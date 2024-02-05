from blog import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name=Lista_de_usuarios)
]
