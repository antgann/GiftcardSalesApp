from django.db import models

# Create your models here.
class EntryModel(models.Model):
    VISA = "Visa"
    MASTERCARD = "Mastercard"
    DISCOVER = "Discover"
    AMEX = "American Express"
    NONE = "-------"
    NETWORK_CHOICES = [
        (VISA, "Visa"),
        (MASTERCARD, "Mastercard"),
        (DISCOVER, "Discover"),
        (AMEX, "American Express"),
        (NONE, "-------"),
    ]
    store_name = models.CharField(max_length=30)
    gift_card_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    network = models.CharField(
        max_length=16,
        choices=NETWORK_CHOICES,
        default=NONE,
    )
    postal_address = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=60)