from django.db import models
from django.utils.text import slugify
from django.conf import settings
from .buyer import Buyer
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    """
    Represents a commodity available for bidding on.
    """
    rating = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    public_review = models.TextField(max_length=500, verbose_name="Description")
    buyer = models.ForeignKey(
        Buyer,
        related_name="reviews",
        on_delete = models.CASCADE
    )

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = slugify(self.name)
        super(Review, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name 