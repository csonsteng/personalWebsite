from django.db import models

class BudgetCategory(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class BudgetSchedule(models.Model):
    schedule_name = models.CharField(max_length=200)
    times_per_year = models.DecimalField(max_digits=10, decimal_places=6)
    times_per_month = models.DecimalField(max_digits=10, decimal_places=6)
    times_per_week = models.DecimalField(max_digits=10, decimal_places=6)
    times_per_day = models.DecimalField(max_digits=10, decimal_places=6)
    period = models.IntegerField(default=0)
    def __str__(self):
        return self.schedule_name

class BudgetItem(models.Model):
    item_name = models.CharField(max_length=200)
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)  #THESE CAN'T CASCADE FIGURE OUT HOW TO USE SET_DEFAULT AND SET A DEFAULT
    value = models.DecimalField(max_digits=10, decimal_places=2)
    schedule = models.ForeignKey(BudgetSchedule, on_delete=models.CASCADE)
    def __str__(self):
        return self.item_name

class AccountType(models.Model):
    type_name = models.CharField(max_length=200)
    def __str__(self):
        return self.type_name

class Account(models.Model):
    account_name = models.CharField(max_length=200)
    type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    account_value = models.DecimalField(max_digits=15,decimal_places=2)
    interest_rate = models.DecimalField(max_digits=7,decimal_places=4)
    def __str__(self):
        return self.account_name
