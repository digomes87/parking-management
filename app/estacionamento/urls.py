from django.urls import path, include
from .views import home, lista_pessoa
urlpatterns = [
    path('', home, name='home'),
    path('pessoas/', lista_pessoa, name='lista_pessoa'),

]
