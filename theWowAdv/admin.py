from django.contrib import admin

from .models import Profile, Advertisement, Response, NewsLetterSubscribedUsers, CategorySubscription
# Register your models here.

admin.site.register(Profile)

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    fields = ('title', 'category','author','body')
    list_display = ('title', 'category','author', )


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    fields = ('advert', 'responseUser', 'title', 'text','isApproved',)
    list_display = ('advert','responseUser', 'title', 'text','isApproved',)


@admin.register(CategorySubscription)
class SubscriptionAdmin(admin.ModelAdmin):
    fields = ('name', 'user')
    list_display = ('name', 'user', )


@admin.register(NewsLetterSubscribedUsers)
class NewsLetterSubscribedUsersAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'dateCreation',)
    list_display = ('name', 'email','dateCreation', )

