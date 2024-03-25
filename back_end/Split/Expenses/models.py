from django.db import models
from Users.models import User, Group

from django.utils.timezone import now
# Create your models here.

class Expense(models.Model):
	name = models.CharField(max_length=255)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	created_by = models.ForeignKey(User, on_delete= models.CASCADE)
	target_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	date = models.DateField(blank=True, default=now)
	status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('PAID', 'Paid')], default='PENDING')  # Track expense status


	def __str__(self): #displays the expense name and the group it belongs to
		return f"Expense: {self.name} (Group: {self.group.name})"

class Contributions(models.Model)