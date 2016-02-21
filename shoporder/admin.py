from django.contrib import admin
from shoporder.models import Order
from shopcart.models import Cart


class OrderAdmin(admin.ModelAdmin):
	list_display = ['name', 'email',  ]	
	class Meta:
		model = Order
	

admin.site.register(Order, OrderAdmin)
