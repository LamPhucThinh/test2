from django.shortcuts import render
from .models import Detail, Expenses
# Create your views here.
def index (request):
    trip = Detail.objects.all()
    price=Expenses.objects.all()
    context = {"name": trip, "price":price}
    return render(request,"detail/index.html", context)
