from django.contrib import admin
from .models import UserProfile, Subscription, VideoCategory, Video

class VideoAdmin(admin.ModelAdmin):

    list_display = ['id']
    list_filter = ['video_category']
   


admin.site.register(UserProfile)
admin.site.register(Subscription)
admin.site.register(VideoCategory)
admin.site.register(Video, VideoAdmin)

