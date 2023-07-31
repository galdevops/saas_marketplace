from django.db import models
from django.utils.text import slugify
from django.conf import settings
from .buyer import Buyer

class GigRequest(models.Model):

    class Status_Types(models.TextChoices):
        published = 'published'
        draft = 'draft'
        diapproved = 'disapproved'
        inactive = 'inactive'

    """
    Represents a commodity available for bidding on.
    """
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, verbose_name="Description")
    # ASK: category/service
    
    buyer = models.ForeignKey(
        Buyer,
        related_name="gigs",
        on_delete = models.CASCADE
    )
    max_budget = models.DecimalField(
        max_digits = 7,
        decimal_places = 2
    )

    flexible_budget = models.BooleanField()

    status = models.CharField(
        max_length=30, choices=Status_Types.choices, default=Status_Types.draft)

    link = models.SlugField(max_length=150, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = slugify(self.name)
        super(GigRequest, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name 