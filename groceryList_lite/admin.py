from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(GroceryList)
admin.site.register(GrocerListContent)
admin.site.register(UsersAndGrocery)
