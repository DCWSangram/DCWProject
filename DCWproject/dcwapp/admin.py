from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CustomerInformation)
class CustomerInformationAdmin(admin.ModelAdmin):
    list_display = [

        'id',
    'user',        
    'full_name',        
    'profile_picture',        
    'mobile_number',        
    'whatsapp_number',        
    'gender',        
    'active',        
    'created_at',        
    'updated_at'       
    ]

@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer_info',
        'appt_name',
        'area',
        'lane_number',
        'block_name',
        'House_no',
        'address_line1',
        'address_line2',
        'city',
        'state',
        'zipcode',
        'created_at',
        'updated_at',
    ]
@admin.register(VehicleDetails)
class VehicleDetailsAdmin(admin.ModelAdmin):
    list_display = [
        'customer_name',
        'vehicle_brand',
        'vehicle_model',
        'vehicle_category',
        'vehicle_number',
        'Fuel_type',
        'vehicle_color',
        'parking_lot_no',
        'parking_area',
        'preferred_time',
        'created_at',
        'updated_at',
    ]
@admin.register(NoOfDays)
class NoOfDaysAdmin(admin.ModelAdmin):
    list_display = [
        'vehicle',
        'start_date',
        'month_end_date',
        'demo_start_date',
    ]