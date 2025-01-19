from django.contrib import admin

from .models import Asset, AssetCategory, CashFlow, CashFlowCategory

# Register your models here.
admin.site.register(Asset)
admin.site.register(AssetCategory)
admin.site.register(CashFlow)
admin.site.register(CashFlowCategory)