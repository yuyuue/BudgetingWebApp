from django.contrib import admin

from .models import Asset, AssetCategory, Cashflow, CashflowCategory

# Register your models here.
admin.site.register(Asset)
admin.site.register(AssetCategory)
admin.site.register(Cashflow)
admin.site.register(CashflowCategory)