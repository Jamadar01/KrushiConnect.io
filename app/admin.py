from django.contrib import admin
from .models import Contact,Medicines,ProductItems,MyOrders,Sell,FarmerProfile,customerProfile
from django.contrib.auth.models import Group

# Create the groups
farmer_group, _ = Group.objects.get_or_create(name='farmers')
customer_group, _ = Group.objects.get_or_create(name='customers')

# Register your models here.
admin.site.register(Contact)
admin.site.register(Medicines)
admin.site.register(ProductItems)
admin.site.register(MyOrders)
admin.site.register(Sell)
admin.site.register(FarmerProfile)
admin.site.register(customerProfile)