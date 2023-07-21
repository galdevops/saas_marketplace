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
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
        size=8,
    )
    link = models.SlugField(max_length=150, blank=True, unique=True)

    def __str__(self):
        return self.user.username 

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = slugify(self.user.username)
        super(Seller, self).save(*args, **kwargs)
