from django.contrib import admin

from .models import MailOrder


class MailOrderAdmin(admin.ModelAdmin):
  list_display = ('nombre', 'email', 'fecha')
  list_filter = ('nombre','fecha')
  search_fields = ('nombre', 'email')
  ordering = ('fecha',)

admin.site.register(MailOrder, MailOrderAdmin)

# Register your models here.
