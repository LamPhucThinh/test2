from django.db import models

# Create your models here.
class Detail (models.Model):
    Name_of_trip = models.CharField(max_length=200)
    Destination = models.CharField(max_length=200)
    Date_of_trip = models.DateTimeField()
    Require_risk_assessment =models.BooleanField()
    Description=models.CharField(max_length=200)

class Expenses (models.Model):
    Type_of_expenses = models.CharField(max_length=200)
    Amount_of_the_expense = models.IntegerField(default=0)
    Time_of_the_expense = models.DateTimeField()
    Name_of_trip = models.ForeignKey(Detail(), on_delete=models.CASCADE)

