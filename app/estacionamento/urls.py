from django.urls import path
from .views import home, lista_pessoa, lista_veiculo, lista_movimento, pessoa_novo, pessoa_update

urlpatterns = [
    path('', home, name='home'),
    path('pessoas/', lista_pessoa, name='lista_pessoa'),
    path('pessoas-novo/', pessoa_novo, name='pessoa_novo'),
    path('update-pessoa/<int:id>', pessoa_update, name='update-pessoa'),
    path('veiculos/', lista_veiculo, name='lista_veiculo'),
    path('movimentos/', lista_movimento),

]
