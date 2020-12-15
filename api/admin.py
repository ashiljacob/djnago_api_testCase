from django.contrib import admin
from .models import Customer

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','address','phoneNumber','gstin','outstandingbalance']
