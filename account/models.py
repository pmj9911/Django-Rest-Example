from django.db import models

# Create your models here.
class UserAccount(models.Model):
	FirstName = models.CharField(max_length=100)
	LastName = models.CharField(max_length=100)
	Email = models.EmailField(max_length=254)