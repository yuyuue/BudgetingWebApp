from django.db import models
from django.urls import reverse

# Create your models here.
class AssetCategory(models.Model):
    name = models.CharField(max_length=50)
    is_credit = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(AssetCategory, on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
    add_date = models.DateTimeField(auto_now_add=True)
    withdrawal_account = models.ForeignKey("self",null=True, on_delete=models.PROTECT)
    payment_due_day = models.IntegerField(null=True)
    payment_confirmation_day = models.IntegerField(null=True)

    def __str__(self):
        return self.name    


class CashflowCategory(models.Model):
    name = models.CharField(max_length=50)
    is_income = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/budgeting/category"


class Cashflow(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(CashflowCategory, on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    date = models.DateTimeField()
    memo = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/budgeting/list"