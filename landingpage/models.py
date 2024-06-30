from django.db import models

class Lead(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.full_name
