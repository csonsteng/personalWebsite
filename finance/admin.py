from django.contrib import admin
from .models import AccountType, Account, Budget, BudgetItem, BudgetSchedule, BudgetCategory

# Register your models here.
admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(BudgetItem)
admin.site.register(BudgetSchedule)
admin.site.register(BudgetCategory)
admin.site.register(Budget)