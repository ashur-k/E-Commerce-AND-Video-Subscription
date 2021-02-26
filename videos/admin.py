from django.contrib import admin
from .models import UserProfile, Subscriptions, VideosCategory, Videos


admin.site.register(UserProfile)
admin.site.register(Subscriptions)
admin.site.register(VideosCategory)
admin.site.register(Videos)

