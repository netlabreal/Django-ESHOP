from django.contrib import admin
from .models import Citem, Cart


class CitemItemsInline(admin.TabularInline):
    model = Citem


class CartAdmin(admin.ModelAdmin):
    inlines = [CitemItemsInline, ]

    list_display = ['user', 'itog', 'timestamp']
    class Meta:
        model = Cart


admin.site.register(Cart, CartAdmin)
