from django.db import models
from django.utils.text import slugify
from django.conf import settings
from .seller import Seller
from apps.accounts.models import User

class Gig(models.Model):

    class Status_Types(models.TextChoices):
        published = 'published'
        draft = 'draft'
        inactive = 'inactive'

    """
    Represents a commodity available for bidding on.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, verbose_name="Description")
    delivery_time = models.IntegerField(null=False, default=1)
    # ASK: category
    # ASK: search tags
    
    seller = models.ForeignKey(
        Seller,
        related_name="gigs",
        on_delete = models.CASCADE
    )

    price = models.DecimalField(
        max_digits = 7,
        decimal_places = 2
    )

    status = models.CharField(
        max_length=30, choices=Status_Types.choices, default=Status_Types.draft)

    link = models.SlugField(max_length=150, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = slugify(self.title)
        super(Gig, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title





class GigUser(models.Model):
    class Meta:
        unique_together = ['user', 'gig']
        db_table = 'gig_user'

    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


