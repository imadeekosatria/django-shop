from django.contrib import admin
from .models import Product, Halaman, Contact, Visitor

class ProductAdmin(admin.ModelAdmin):
  list_display = ('nama', 'visitor_product', 'updated_at')
  prepopulated_fields = {'slug': ('nama',)}

class ContactAdmin(admin.ModelAdmin):
  list_display = ('created_at', 'count')

class HalamanAdmin(admin.ModelAdmin):
  list_display = ('nama_web', 'created_at', 'updated_at')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Halaman, HalamanAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Visitor)
