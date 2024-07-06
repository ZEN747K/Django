from django.contrib import admin
from cards.models import GPUs,users_info,Store
from django.utils.html import format_html
# Register your models here.


class GPUsAdmin(admin.ModelAdmin):
    
    search_fields = ['model','gpu_model']
    
    list_filter = ['brand','gpu_model']
    list_display=['brand','Image','GPU_id','model','chipset','gpu_model','warranty_years','last_modified_by','last_modified_at']
    list_editable=['warranty_years']
    
admin.site.register(GPUs, GPUsAdmin)





admin.site.register(users_info)
class StoreAdmin(admin.ModelAdmin):
    
    search_fields =['store_name']
    list_display=['store_name','store_num','gpu','products','last_modified_by','last_modified_at']
    list_filter = ['gpu','products']
    list_editable=['products']
    
    autocomplete_fields = ['gpu']


admin.site.register(Store,StoreAdmin)