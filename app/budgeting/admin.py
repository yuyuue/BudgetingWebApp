from django.contrib import admin

from .models import Asset, AssetCategory, Credit

# Register your models here.
admin.site.register(Asset)
admin.site.register(AssetCategory)
admin.site.register(Credit)