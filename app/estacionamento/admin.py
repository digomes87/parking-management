from django.contrib import admin
from .models import Marca, Pessoa, Veiculo, Paramentros, MovRotativo, Mensalista, MovMensalista


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'veiculo', 'pago', 'total')


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto', 'dt_pgto')


admin.site.register(Marca)
admin.site.register(Pessoa)
admin.site.register(Veiculo)
admin.site.register(Paramentros)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)