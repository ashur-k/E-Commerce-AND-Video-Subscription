from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


SUBSCRIPTIONS = (
    ('F', 'FREE'),
    ('M', 'MONTHLY'),
    ('Y', 'YEARLY'),
    )


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(blank=False, upload_to='user_images/')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    address_line_1 = models.CharField(max_length=80, null=True, blank=True)
    address_line_2 = models.CharField(max_length=80, null=True, blank=True)
    county_town_or_city = models.CharField(max_length=80, null=True, blank=True)
    postal_or_zip_code = models.CharField(max_length=20, null=True, blank=True)


class Subscriptions(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    has_subscription = models.BooleanField(default=False)
    subscription_start_date = models.DateField(null=True, blank=True)
    subscription_expiry_date = models.DateField(null=True, blank=True)
    subscription_type = models.CharField(max_length=100, choices=SUBSCRIPTIONS, default='FREE')
    subscription_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)


class VideosCategory(models.Model):
    video_category = models.CharField(max_length=254)
    image = models.ImageField(blank=False, upload_to='video_category_images/')
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.video_category)
        super(VideosCategory, self).save(*args, **kwargs)
        print(self.slug)
    
    def __str__(self):
        return self.video_category


class Videos(models.Model):
    video_category = models.ForeignKey(VideosCategory, null=True, blank=True, on_delete=models.SET_NULL)
    video_name = models.CharField(max_length=30)
    video_description = models.CharField(max_length=255)
    video_URL = models.URLField(max_length=300)
    is_free_video = models.BooleanField(default=False)
    

