from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Account, AccountType, Budget, BudgetItem, AccountData, BudgetSchedule, BudgetCategory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def loginUser(request):
    if request.method=='POST':
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return index(request)
        else:
            context={
                'fail': 'incorrect username or password.',
                }
            return render(request, 'finance/login.html', context)
    else:
        return render(request, 'finance/login.html')


@login_required
def accounts(request):
    context = {}
    if request.method == 'POST':
        a = Account()
        a.aName = request.POST['aName']
        d = AccountData()
        d.value = request.POST['value']
        d.iRate = request.POST['interest']
        tpk = request.POST['type']
        try:
            t = AccountType.objects.get(pk=tpk)
            a.type = t
        except:
            pass
        a.user = request.user
        a.save()
        d.refAccount = a
        d.save()
        a.lastDatum = d
        a.save()

    accountList = Account.objects.filter(user=request.user)
    savingsList = accountList.filter(type=AccountType.objects.get(tName='Savings'))
    creditList = accountList.filter(type=AccountType.objects.get(tName='Credit'))
    investmentList = accountList.filter(type=AccountType.objects.get(tName='Investment'))
    accountTypes = AccountType.objects.all()
    context['accountList'] = accountList
    context['savingsList'] = savingsList
    context['creditList'] = creditList
    context['investmentList'] = investmentList
    context['accountTypes'] = accountTypes
    return render(request,'finance/accounts.html', context)

@login_required
def index(request):

    return render(request, 'finance/finance.html')

@login_required
def budget(request):
    context = {
        'schedules': BudgetSchedule.objects.all(),
    }
    if request.method == 'POST':
        post = request.POST
        try:
            budget = Budget.objects.get(pk=post['budgetID'])
            categories = BudgetCategory.objects.filter(budget=budget)
            categories.delete()
            newCategory = BudgetCategory()
            newCategory.category_name = 'Income'
            newCategory.budget = budget
            newCategory.save()
            newCategory = BudgetCategory()
            newCategory.category_name = 'Essentials'
            newCategory.budget = budget
            newCategory.save()
        except:
            budget = Budget()
            budget.budget_name = 'No way to specify this yet'
            budget.save()
        itemCount = int(post['itemCount'])
        for n in range(itemCount):
            i = str(n)
            newItem = BudgetItem()
            newItem.item_name = post['iName_'+i]
            categoryName = post['iCategory_'+i]
            scheduleName = post['iPeriod_'+i]
            newItem.value = post['iValue_'+i]
            category = BudgetCategory.objects.filter(budget=budget,category_name=categoryName)
            if category:
                newItem.category = category[0]
            else:
                newCategory = BudgetCategory()
                newCategory.category_name = categoryName
                newCategory.budget = budget
                newCategory.save()
                newItem.category = newCategory
            schedule = BudgetSchedule.objects.filter(schedule_name=scheduleName)[0]
            newItem.schedule = schedule
            newItem.save()
        categories = BudgetCategory.objects.filter(budget=budget)
        items = BudgetItem.objects.filter(category__in=categories)
        context['categories'] = categories
        context['items'] = items
        context['budget'] = budget

    return render(request, 'finance/budget.html', context)

@login_required
def budget_item(request, item_id):
    item = get_object_or_404(BudgetItem, pk=item_id)
    if item.value < 0:
        value = "-$" + str(-1*item.value)
    else:
        value = "$" + str(item.value)
    output = {
        'name' : item.item_name,
        'value' : value,
    }
    context = {
        'item' : output,
    }
    return render(request, 'finance/budget_item.html', context)
