from django.contrib import admin
from .models import  Grosor, Color, Producto, ImagenProducto

# Register your models here.


class GrosorInline(admin.TabularInline):
    model = Grosor

class ColorInline(admin.TabularInline):
    model = Color
class ImageInline(admin.TabularInline):
    model = ImagenProducto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)
    inlines = [GrosorInline, ImageInline]

class GrosorAdmin(admin.ModelAdmin):
    list_display = ('product', 'grosor', 'precio')
    list_filter = ('product',)
    search_fields = ('product', 'grosor')
    ordering = ('product',)
    inlines = [ColorInline] 

class ColorAdmin(admin.ModelAdmin):
    list_display = ('grosor', 'color')
    list_filter = ('grosor',)
    search_fields = ('grosor', 'color')
    ordering = ('grosor',)
    
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Grosor, GrosorAdmin)
admin.site.register(Color, ColorAdmin) 

