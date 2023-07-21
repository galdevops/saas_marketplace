from django.db import models
from .seller import Seller
from .gig_request import GigRequest

class Bid(models.Model):
    seller = models.ForeignKey(
        Seller, 
        related_name = "seller",
        on_delete = models.CASCADE
    )
    gig_request = models.ForeignKey(
        GigRequest, 
        related_name = "gig_requests",
        on_delete = models.CASCADE
    )
    amount = models.DecimalField(
        decimal_places = 2, 
        verbose_name="Bid Amount",
        max_digits = 7)
    bid_date = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ['amount','bid_date']

    def __str__(self):
        return "%s on %s" % (self.amount, self.product.name)
