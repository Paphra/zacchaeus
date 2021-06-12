from statements.calculations import totals, values 
from .models import OtherIncomeTaxRange

def calculator(person, tax_ranges, sDate, eDate):
	values = totals(person, sDate, eDate)
	tax_range = tax_ranges.first()
	net_profit = values['net_profit']

	for rg in tax_ranges:
		if net_profit > rg.low and net_profit < rg.high:
			tax_range = rg

	tax = net_profit * (tax_range.percentage / 100)
	tax = tax + tax_range.addition
	gross_tax = tax - tax_range.subtraction

	interests = values['interests']
	property_incomes = values['property_incomes']
	
	other_ranges = OtherIncomeTaxRange.objects.filter(is_active=True)
	interest_range = None
	property_range = None
	interest_tax = 0
	interest_chargeable = 0

	property_tax = 0
	property_chargeable = 0
	
	for rg in other_ranges:
		if rg.name.find('interest') > -1 or rg.name.find('Interest') > -1:
			interest_range = rg
			if rg.threshhold < interests:
				interest_chargeable = interests - rg.threshhold
				interest_tax = interest_chargeable * rg.percentage
				interest_tax = interest_tax - rg.subtraction + rg.addition

		if rg.name.find('property') > -1 or rg.name.find('Property') > -1:
			property_range = rg
			if rg.threshhold < property_incomes:
				property_chargeable = property_incomes - rg.threshhold
				property_tax = property_chargeable * rg.percentage
				property_tax = property_tax - rg.subtraction + rg.addition

	net_tax = tax + interest_tax + property_tax

	return {
		'totals': values,
		'tax_range': tax_range,
		'other_ranges': other_ranges,
		'interest_range': interest_range,
		'property_range': property_range,

		'interest_tax': interest_tax,
		'interest_chargeable': interest_chargeable,

		'property_tax': property_tax,
		'property_chargeable': property_chargeable,

		'gross_tax': gross_tax,
		'net_tax': net_tax,
	}
