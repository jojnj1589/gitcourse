from django.contrib import admin

# Register your models here.

from pedidos.models import clientes,articulos,pedidos

class clientesadmin(admin.ModelAdmin):
    """docstring for clientesadmin."""

    list_display=("name","addres")
    search_fields=("name", "addres")

class artiadmin(admin.ModelAdmin):
    """docstring for artiadmin."""

    list_display=("name", "seccion", "precio")
    list_filter=("seccion",)

class pediadmin(admin.ModelAdmin):
    """docstring for pediadmin."""

    list_display=("id","delivered")
    list_filter=("date","delivered",)
    date_hierarchy="date"


admin.site.register(clientes, clientesadmin)
admin.site.register(articulos, artiadmin)
admin.site.register(pedidos, pediadmin)
