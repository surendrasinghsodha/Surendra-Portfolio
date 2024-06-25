from django.db import models
from django.core.mail import send_mail
from django.conf import settings

from myapp.utils import custom_send_mail


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
