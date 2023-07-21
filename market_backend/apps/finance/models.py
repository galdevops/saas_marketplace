from django.db import models

class PaymentMethod(models.Model):
    pass

class BillingInfo(models.Model):
    full_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    