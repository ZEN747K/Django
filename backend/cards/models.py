from django.db import models

# Create your models here.

class GPUs(models.Model):
    products_id = models.AutoField(primary_key=True)
    GPU_id = models.CharField(max_length=255,default='default_value')
    products = models.PositiveIntegerField()
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    slot = models.CharField(max_length=255)
    chipset = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    gpu_model = models.CharField(max_length=255)
    gpu_speed_oc = models.PositiveIntegerField()
    gpu_speed_gaming = models.PositiveIntegerField()
    memory_speed = models.PositiveIntegerField()
    memory_size = models.PositiveIntegerField()
    memory_type = models.CharField(max_length=255)
    cuda_cores = models.PositiveIntegerField()
    length = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    max_resolution = models.CharField(max_length=255)
    directx_support = models.CharField(max_length=255)
    crossfire_sli_support = models.CharField(max_length=255)
    dvi_port = models.PositiveIntegerField()
    hdmi_port = models.PositiveIntegerField()
    display_port = models.PositiveIntegerField()
    option_port = models.CharField(max_length=255)
    power_consumption = models.CharField(max_length=255)
    power_supply_requirement = models.PositiveIntegerField()
    power_connectors = models.CharField(max_length=255)
    warranty_years = models.PositiveIntegerField()
    note = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.model

class users_info(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.display_name




class AdminInfo(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    time_login = models.DateTimeField()

    def __str__(self):
        return self.email


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_num = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    graphics_card_id = models.PositiveIntegerField()

    def __str__(self):
        return self.store_name
    