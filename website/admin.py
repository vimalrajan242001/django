from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

#for admin portal headings

admin.site.site_header = "Ausweg Automations"
admin.site.site_title = "Ausweg Automations Admin Portal"
admin.site.index_title = "Welcome to Ausweg Automations"