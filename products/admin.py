from django.contrib import admin
from .models import Product

# admin.site.register(Product)

# Кастомизация админки
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'category', 'count',]
	list_filter = ['category']
	# search_fields = ['name__startswith']
	search_fields = ['name']