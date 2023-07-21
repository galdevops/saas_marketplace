from django.db import models
from .buyer import Buyer
from .gig import Gig

class Order(models.Model):

    class Status_Types(models.TextChoices):
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
    total_amount = models.DecimalField(
        decimal_places = 2, 
        verbose_name="Total Amount",
        max_digits = 7)
    order_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=30, choices=Status_Types.choices, default=Status_Types.in_progress)

    class Meta:
        ordering = ['total_amount','order_date']

    def __str__(self):
        return "%s on %s" % (self.total_amount, self.gig.title)
