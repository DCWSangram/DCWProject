from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,time

# Create your models here.
class CustomerInformation(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="custuser")
    full_name = models.CharField("Full Name",max_length = 150)
    country_code = models.IntegerField(default=91)
    mobile_number = models.CharField(max_length=10, unique=True)
    whatsapp_number = models.CharField(max_length=10,null=True,unique=True,blank=True)
    gender = models.CharField(max_length=11, choices=[('male','Male'),('female','FeMale'),('transgender','Transgender')])
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField('Profile Picture',blank=True,upload_to='images')
    
    def __str__(self):
        return f"{self.full_name}"
    class Meta:
        verbose_name_plural = "Customer Information"

class CustomerAddress(models.Model):
    customer_info = models.OneToOneField(CustomerInformation,related_name='cinfo', on_delete=models.CASCADE)
    appt_name = models.CharField(max_length=100, blank=True)
    area = models.CharField(max_length = 150,blank=True)
    lane_number = models.CharField(max_length = 150,blank=True)
    block_name = models.CharField('Block Number/ Tower No',max_length=40, blank=True)
    House_no = models.CharField('House Number/ Unit No',max_length=40)
    address_line1 = models.CharField(max_length=250)
    address_line2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    zipcode = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.customer_info} {self.appt_name}"
    class Meta:
        verbose_name_plural = "Customer Address"
    
class VehicleDetails(models.Model):
    customer_name = models.ForeignKey(CustomerInformation,on_delete=models.CASCADE)
    vehicle_brand = models.CharField('Brand', max_length=100)
    vehicle_model = models.CharField('Model', max_length=100)
    vehicle_category = models.CharField('Category', max_length=100)
    vehicle_number = models.CharField('Vehicle Number', max_length=250)
    Fuel_type = models.CharField('Fuel Type', max_length=250, blank=True)
    vehicle_color = models.CharField('Vehicle Color', max_length=250)
    parking_lot_no = models.CharField('Parking Lot No',max_length=250)
    parking_area = models.CharField('Parking area', max_length=250, blank=True)
    preferred_time = models.TimeField('Preferred Time',default=time(9, 00, 00))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Vehicle Details"
    def __str__(self):
        return f"{self.customer_name}"
    
class NoOfDays(models.Model):
    vehicle = models.OneToOneField(VehicleDetails,on_delete = models.CASCADE,related_name="noofdays")
    start_date = models.DateField()
    month_end_date = models.DateField()
    demo_start_date = models.DateField()
