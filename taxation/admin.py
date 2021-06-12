from django.contrib import admin
from .models import PersonType, IncomeTaxRange, OtherIncomeTaxRange

@admin.register(PersonType)
class PersonTypeAdmin(admin.ModelAdmin):
	list_display = ['name', 'description', 'is_active', 'updated', 'created']
	list_filter = ['is_active', 'updated']
	search_fields = ['name', 'description']

@admin.register(IncomeTaxRange)
class IncomeTaxRangeAdmin(admin.ModelAdmin):
	list_display = ['name', 'person_type', 'low', 'high', 'subtraction', 'addition', 'is_active', 'percentage', 'updated', 'created']
	list_filter = ['is_active', 'person_type', 'updated']
	list_editable = ['is_active', 'percentage']
	search_fields = ['name']

@admin.register(OtherIncomeTaxRange)
class OtherIncomeTaxRangeAdmin(admin.ModelAdmin):
	list_display = ['name', 'person_type', 'threshhold', 'subtraction', 'addition', 'is_active', 'percentage', 'updated', 'created']
	list_filter = ['is_active', 'person_type', 'updated']
	list_editable = ['is_active', 'percentage']
	search_fields = ['name']
