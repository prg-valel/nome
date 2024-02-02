from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('cadastro', views.cadastro),
    path('tabela', views.tabela)
]
