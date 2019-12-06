from django.contrib import admin
from .models import RegularPizza,SicilianPizza,Toppings,Pasta,Salads,DinnerPlatters,Subs,Order,Confirmed_order

# Register your models here.

admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Toppings)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(Subs)
admin.site.register(Order)
admin.site.register(Confirmed_order)