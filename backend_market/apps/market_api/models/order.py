from django.db import models
from django.utils.text import slugify
from .buyer import Buyer
from .gig import Gig
import time
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver


class Order(models.Model):

    class Status_Types(models.TextChoices):
        pending = 'pending'
        incomplete = 'incomplete'
        in_progress = 'in progress'
        delivered = 'delivered'
        rejected = 'rejected'
        # in_revision = 'in revision'
        completed = 'completed'
        dispute = 'dispute'
        late = 'late'
        # ASK: relevancy of status

    buyer = models.ForeignKey(
        Buyer, 
        related_name = "buyers",
        on_delete = models.CASCADE
    )

    gig = models.ForeignKey(
        Gig, 
        related_name = "gigs",
        on_delete = models.CASCADE
    )

    total_cost = models.DecimalField(
        decimal_places = 2, 
        verbose_name="Total Cost",
        max_digits = 7, default=0.00)

    
    amount = models.IntegerField(null=False, default=1)
    
    due_date = models.DateTimeField(blank=True, null=True)

    order_date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=30, choices=Status_Types.choices, default=Status_Types.pending)
    
    link = models.SlugField(max_length=150, blank=True, unique=True)

    def save(self, *args, **kwargs):        
        if not self.link:
            timed = str(time.time()).split('.')[0]
            seller = str(self.gig.seller.user.email).split('@')[0]
            slugged = timed + seller
            self.link = slugify(slugged)
        super(Order, self).save(*args, **kwargs)
        

    class Meta:
        ordering = ['total_cost','order_date']

    def __str__(self):
        return "%s on %s" % (self.total_cost, self.gig.title)