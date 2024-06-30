from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, max_length=255, null=True, blank=True)
    territory = models.CharField(max_length=5)

    def __str__(self):
        return self.user.username
