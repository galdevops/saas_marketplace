from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Seller(models.Model):
    """
    A User who creates an account on the platform with the intent to offer Products to other users
    to be bid on.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        related_name = "seller",
        on_delete = models.CASCADE
    )
    description = models.CharField()
    skills = ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        )
    
    link = models.SlugField(max_length=150, blank=True, unique=True)

    def __str__(self):
        return self.user.email 

    def save(self, *args, **kwargs):
        if not self.link:
            str_email = str(self.user.email).split('@')[0]
            self.link = slugify(str_email)
        super(Seller, self).save(*args, **kwargs)
