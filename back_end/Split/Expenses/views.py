from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Expense
from Users.models import User, Group
# Create your views here.

def index(request):
	categories = category.objects.all()

	return render(request, 'Expenses/index.html')

def create_expense(request):
	group = Group.objects.get(pk=group_id)

	if request.method == 'POST':
		name = request.POST['name']
		amount = request.POST['amount']
		


