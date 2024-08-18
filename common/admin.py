from django.contrib import admin
from common.models import Endereco

class Enderecos(admin.ModelAdmin):
    list_display = ('id', 'logradouro', 'numero', 'cep', 'bairro', 'cidade', 'estado', 'complemento')
    list_display_links = ('id', 'logradouro',)
    search_fields = ('logradouro',)
admin.site.register(Endereco, Enderecos)