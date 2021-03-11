from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from embed_video .fields import EmbedVideoField


SUBSCRIPTIONS = (
    ('F', 'FREE'),
    ('M', 'MONTHLY'),
    ('Y', 'YEARLY'),
    )


class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'UserProfiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(blank=False, upload_to='user_images/')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    address_line_1 = models.CharField(max_length=80, null=True, blank=True)
    address_line_2 = models.CharField(max_length=80, null=True, blank=True)
    county_town_or_city = models.CharField(max_length=80, null=True, blank=True)
    postal_or_zip_code = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Subscription(models.Model):

    class Meta:
        verbose_name_plural = 'Subscriptions'

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    has_subscription = models.BooleanField(default=False)
    subscription_start_date = models.DateField(null=True, blank=True)
    subscription_expiry_date = models.DateField(null=True, blank=True)
    subscription_type = models.CharField(max_length=100, choices=SUBSCRIPTIONS, default='FREE')
    subscription_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username


class VideoCategory(models.Model):

    class Meta:
        verbose_name_plural = 'VideoCategories'

    video_category = models.CharField(max_length=254)
    image = models.ImageField(blank=False, upload_to='video_category_images/')
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.video_category)
        super(VideoCategory, self).save(*args, **kwargs)
        print(self.slug)
    
    def __str__(self):
        return self.video_category


class Video(models.Model):

    class Meta:
        verbose_name_plural = 'Videos'
        ordering = ['-video_added']

    video_category = models.ForeignKey(VideoCategory, null=True, blank=True, on_delete=models.SET_NULL)
    video_image_thumbnail = models.ImageField(blank=True, upload_to='video_category_images/image_thumbnails')
    video_name = models.CharField(max_length=30)
    video_description = models.CharField(max_length=255)
    video_URL = EmbedVideoField()
    is_free_video = models.BooleanField(default=False)
    video_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.video_name)
    
    def delete(self, *args, **kwargs):
        self.video_image_thumbnail.delete()
        super().delete(*args, **kwargs)
