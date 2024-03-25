import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
	phone = models.CharField(max_length=10, unique=True)
	pin = models.CharField(max_length=4)
	def __str__(self):
		return self.username

class Group(models.Model):
	name = models.CharField(max_length=20, default='name')
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	members = models.ManyToManyField(User, related_name='groups_joined')

	def __str__(self):
		return self.name

