from django.db import models
from django.utils.text import slugify
from django.conf import settings
from .order import Order
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    """
    Represents a commodity available for bidding on.
    """
    delivery_rating = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=True)
    
    expectations_rating = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=True)

    needs_rating = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=True)
    
    seller_rating = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=True)

    public_review = models.TextField(max_length=500, verbose_name="Description", null=True)

    
    order = models.ForeignKey(
        Order,
        related_name="reviews",
        on_delete = models.CASCADE, null=False
    )

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.order 