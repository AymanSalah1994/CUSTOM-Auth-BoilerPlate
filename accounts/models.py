from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    mobileNumber = models.CharField(max_length=11, blank=True, null=True)
    is_merchant = models.BooleanField(default=False)
    city = models.CharField(max_length=50, blank=True, null=True)
    # Below are made to set email as the Creditintial for the User
    # username = None
    # email = models.EmailField(_('email address'), unique=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []