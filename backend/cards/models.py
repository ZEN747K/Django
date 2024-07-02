from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class GPUs(models.Model):
    products_id = models.AutoField(primary_key=True)
    GPU_id = models.CharField(max_length=255,)
    
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
    image = models.ImageField(upload_to='gpu_images/', blank=True, null=True)
   
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_modified_at = models.DateTimeField(auto_now=True)
     

    def save(self, *args, **kwargs):
        self.last_modified_at = timezone.now()
        super(GPUs, self).save(*args, **kwargs)
    

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







class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_num = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    graphics_card_id = models.PositiveIntegerField(null=True)
    products=models.PositiveIntegerField()
    gpu = models.ForeignKey('GPUs', on_delete=models.CASCADE)
    last_modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='store_modified_by')
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_modified_by = models.ForeignKey(User, related_name='modified_users', on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.user.username

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()