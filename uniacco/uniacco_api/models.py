from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class UserLoginHistory(models.Model):
    # For every login ip address is stored in this model
    ip_address = models.CharField(max_length=100)