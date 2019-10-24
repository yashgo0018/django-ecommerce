from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save

User = get_user_model()


class BillingProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()


class BillingProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255, default="India")
    pincode = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = BillingProfileManager()

    def __str__(self):
        return self.email


# def user_created_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         BillingProfile.objects.get_or_create(
#             user=instance, email=instance.email)


# post_save.connect(user_created_receiver, sender=User)
