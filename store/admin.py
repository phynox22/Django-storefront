from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
 list_display = ['title', 'unit_price', 'inventory_status','collection_title']
 list_editable = ['unit_price']
 list_per_page = 10
 list_select_related = ['collection']
 
 def collection_title(self, product):
     return product.collection.title

 @admin.display(ordering='inventory') 
 def inventory_status(self, product):
    if product.inventory < 10:
      return 'low'
    return  'ok'  

admin.site.register(models.Collection)

admin.site.register(models.Product, ProductAdmin)
