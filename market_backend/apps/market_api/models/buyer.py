from django.db import models
from django.utils.text import slugify
from django.conf import settings

class Buyer(models.Model):
    """
    A Profile for a user who registers with the intent to bid on a Product/commodity.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        related_name = "buyer",
        on_delete =  models.CASCADE
    )

    link = models.SlugField(max_length=150, blank=True, unique=True)

    def __str__(self):
        return self.user.username 

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = slugify(self.user.username)
        super(Buyer, self).save(*args, **kwargs)
