from django.db import models

# Create your models here.
class AssetCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(AssetCategory, on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
    add_date = models.DateTimeField(auto_now_add=True)
    is_credit = models.BooleanField(default=False)
    withdrawal_account = models.ForeignKey('self', null=True, on_delete=models.PROTECT)
    payment_due_date = models.DateTimeField(null=True)
    payment_confirmation_date = models.DateField(null=True)

    def __str__(self):
        return self.name


class CashFlowCategory(models.Model):
    name = models.CharField(max_length=50)
    is_income = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CashFlow(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(CashFlowCategory, on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    date = models.DateTimeField()
    memo = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.name