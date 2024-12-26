from django.db import models

# Create your models here.
class AssetCategory(models.Model):
    name = models.CharField(max_length=50)
    is_credit = models.BooleanField


class Asset(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(AssetCategory, on_delete=models.PROTECT)
    amount = models.IntegerField
    add_date = models.DateTimeField(auto_now_add=True)


class Credit(models.Model):
    withdrawal_account = models.ForeignKey(AssetCategory, on_delete=models.PROTECT)
    payment_due_date = models.DateTimeField
    payment_confirmation_date = models.DateField


class IncomeCategory(models.Model):
    pass


class Income(models.Model):
    pass


class ExpenceCategory(models.Model):
    pass


class Expence(models.Model):
    pass