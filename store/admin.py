from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Product
from .models import Collection

# Register your models here.


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['price', 'title', 'collection', 'inventory_status', 'collection']
    list_per_page = 10
    search_fields = ['title']

    @admin.display(ordering='inventory')
    def inventory_status(self, product: Product):
        if product.inventory < 20:
            return 'Low'
        return 'Ok'


@admin.register(Collection)
class CollectionAdmin(ModelAdmin):
    list_display = ['id', 'title', 'inventory_count']

    def inventory_count(self, collection: Collection):
        return collection.product_set.count()
