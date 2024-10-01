from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Account(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email  = models.EmailField(max_length=254)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email