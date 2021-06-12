from sales.models import Sale, SalesReturn
from purchases.models import Purchase, PurchasesReturn
from expenses.models import Depreciation, Expense
from incomes.models import Interest, Income, PropertyIncome
from assets.models import Debtor, Asset
from liabilities.models import Creditor, Liability, Withdrawal
from stock.models import OpeningStock, ClosingStock


def values(person, model, sDate=None, eDate=None):
    total = 0
    
    if sDate and eDate:
        items = model.objects.filter(
            person=person,
            date_made__range=[sDate+'T00:00:00+0300', eDate+'T23:59:59+0300']
        )
    else:
        items = model.objects.filter(
            person=person,
        ).all()

    for item in items:
        total += item.amount
    
    return total

def totals(person, sDate, eDate):

    sales = values(person, Sale, sDate, eDate)
    sales_returns = values(person, SalesReturn, sDate, eDate)
    purchases = values(person, Purchase, sDate, eDate)
    purchases_returns = values(person, PurchasesReturn, sDate, eDate)
    expenses = values(person, Expense, sDate, eDate)
    incomes = values(person, Income, sDate, eDate)
    interests = values(person, Interest, sDate, eDate)
    property_incomes = values(person, PropertyIncome, sDate, eDate)

    assets = values(person, Asset)
    liabilities = values(person, Liability)
    depreciations = values(person, Depreciation)
    debtors = values(person, Debtor)
    creditors = values(person, Creditor)
    withdrawals = values(person, Withdrawal)
    
    opening_stock = OpeningStock.objects.filter(
        person=person,
        date_made__range=[sDate+'T00:00:00+0300', eDate+'T23:59:59+0300']
        ).first()

    if opening_stock:
        opening_stock = opening_stock.amount 
    else:
        opening_stock = 0

    closing_stock = ClosingStock.objects.filter(
        person=person,
        date_made__range=[sDate+'T00:00:00+0300', eDate+'T23:59:59+0300']
        ).last()

    if closing_stock:
        closing_stock = closing_stock.amount 
    else:
        closing_stock = 0

    owners_equity = liabilities + creditors + interests + property_incomes - withdrawals
    
    net_sales = sales - sales_returns
    net_purchases = purchases - purchases_returns

    GAFS = opening_stock + net_purchases
    cost_of_sales = GAFS - closing_stock

    gross_profit = net_sales - cost_of_sales
    total_income = incomes + gross_profit

    net_profit = total_income - expenses
    total_assets = assets + debtors + net_profit - depreciations

    gap = total_assets - owners_equity

    return {
        'sales': sales,
        'sales_returns': sales_returns,
        'net_sales': net_sales,
        'purchases': purchases,
        'purchases_returns': purchases_returns,
        'net_purchases': net_purchases,
        'expenses': expenses,
        'incomes': incomes,

        'gafs': GAFS,

        'assets': assets,
        'liabilities': liabilities,
        'opening_stock': opening_stock,
        'closing_stock': closing_stock,

        'cost_of_sales': cost_of_sales,
        'gross_profit': gross_profit,
        'total_income': total_income,

        'creditors': creditors,
        'debtors': debtors,
        'net_profit': net_profit,
        'total_assets': total_assets,
        'depreciations': depreciations,
        'interests': interests,
        'property_incomes': property_incomes,
        'owners_equity': owners_equity,
        'withdrawals': withdrawals,
        'gap': gap,
    }
