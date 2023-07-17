from django.contrib import admin

from .models import Advertisement, Response
# Register your models here.

# admin.site.register(Advertisement)

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    fields = ('title', 'category','author',)
    list_display = ('title', 'category','author', )


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    fields = ('responseAdvertisement', 'responseUser', 'text','approved',)
    list_display = ('responseAdvertisement','responseUser', 'text','approved',)