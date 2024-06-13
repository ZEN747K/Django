from django.contrib import admin
from cards.models import GPUs,users_info,AdminInfo,Store
# Register your models here.
admin.site.register(GPUs)

admin.site.register(users_info)

admin.site.register(AdminInfo)

admin.site.register(Store)