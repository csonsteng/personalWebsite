from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Account, AccountType, BudgetItem

def accounts(request):
    account_list = Account.objects.order_by('type')
    output_list = []
    for a in account_list:      #FIGURE OUT PROPER NUMBER FORMATTING WITH COMMAS
        if a.account_value < 0:
            value = "-$" + str(-1*a.account_value)
        else:
            value = "$" + str(a.account_value)
        output = {
            'name' : a.account_name,
            'value' : value,
        }
        output_list.append(output)
    context = {
        'account_list' : output_list,
    }
    return render(request,'budget/accounts.html', context)

def index(request):
    return HttpResponse("This is the index.")

def budget(request, schedule_id):
    return HttpResponse("This shows the budget at a %s breakdown" % schedule_id)

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
    return render(request,'budget/budget_item.html', context)
