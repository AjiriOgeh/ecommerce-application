from django.db.models.signals import post_save
from django.dispatch import receiver

from ecommerce.models import ShoppingCart
from user.models import Customer


@receiver(post_save,sender=Customer)
def add_cart(created,instance, **kwargs):
    if created:
        ShoppingCart.objects.create(
            customer=instance
        )