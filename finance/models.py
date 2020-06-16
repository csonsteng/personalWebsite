from django.db import models
from django.contrib.auth.models import User

class Budget(models.Model):
    budget_name = models.CharField(max_length=200)

class BudgetCategory(models.Model):
    category_name = models.CharField(max_length=200)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.category_name

class BudgetSchedule(models.Model):
    schedule_name = models.CharField(max_length=200)
    period = models.IntegerField(default=0)
    def times_per_year(self):
        return self.period
    def times_per_month(self):
        return self.period/12
    def times_per_week(self):
        return self.period/52
    def times_per_day(self):
        return self.period/365

    def __str__(self):
        return self.schedule_name

class BudgetItem(models.Model):
    item_name = models.CharField(max_length=200)
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    schedule = models.ForeignKey(BudgetSchedule, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.item_name

class AccountType(models.Model):
    tName = models.CharField(max_length=200)
    def __str__(self):
        return self.tName

class Account(models.Model):
    aName = models.CharField(max_length=200)
    type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    lastDatum = models.ForeignKey('AccountData', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.aName

class AccountData(models.Model):
    refAccount = models.ForeignKey(Account, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=15,decimal_places=2)
    iRate = models.DecimalField(max_digits=7,decimal_places=4)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return str(self.date) + " : " + str(self.value)

