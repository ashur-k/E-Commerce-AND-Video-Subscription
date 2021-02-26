from django.db import models


PARENT_NAMES = (
        ('clothing', 'clothing'),
        ('homeware', 'homeware'),
        ('discount-offers', 'discount-offers'),
        ('new-arrivals', 'new-arrivals'),
    )

STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    parent_name = models.CharField(max_length=25, choices=PARENT_NAMES)
    name = models.CharField(max_length=254)
    image = models.ImageField(blank=False, upload_to='category_imgs/')
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name