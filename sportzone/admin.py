from django.contrib import admin
from.models import *

admin.site.register(CustomerApplicantTable)

admin.site.register(Customer)

admin.site.register(Product)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Tags)
