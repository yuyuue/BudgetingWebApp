from django.contrib import admin

from .models import Asset, AssetCategory

# Register your models here.
admin.site.register(Asset)
admin.site.register(AssetCategory)