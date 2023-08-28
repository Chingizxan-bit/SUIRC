from django.contrib import admin
from .models import Advertisement
from django.utils import timezone
# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display =[ 'title', 'content', 'price', 'created_date', 'user', 'auction', 'location',  'category', 'photo']
    list_filter = ['auction']
    auctions= ['forbid_the_auction', 'permit_the_auction']
    fieldsets = (
        ('Общее', {
          'fields': ('title', 'content', 'user', 'category', 'location', 'photo'),
          'classes': ['collapse']
        }),
         ('Финансы', {
          'fields': ('price', 'auction'),
          'classes': ['collapse']
        }),
       
    
    )
   
   
    @admin.action(description="Убрать возможность торга")  
    def forbid_the_auction(self, request, queryset):
       queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")  
    def permit_the_auction(self, request, queryset):
       queryset.update(auction=True)
       
 

admin.site.register(Advertisement, AdvertisementAdmin) 