from django.contrib import admin
from .models import UserProfile, Subscription, VideoCategory, Video


admin.site.register(UserProfile)
admin.site.register(Subscription)
admin.site.register(VideoCategory)
admin.site.register(Video)

