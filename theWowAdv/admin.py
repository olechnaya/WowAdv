from django.contrib import admin

from .models import Advertisement, Response
# Register your models here.

# admin.site.register(Advertisement)

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    fields = ('title', 'category','author','body')
    list_display = ('title', 'category','author', )


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    fields = ('advert', 'responseUser', 'title', 'text','approved',)
    list_display = ('advert','responseUser', 'title', 'text','approved',)