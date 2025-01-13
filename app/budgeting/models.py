from django.db import models

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

    def __str__(self):
        return self.name

class Credit(models.Model):
    asset = models.OneToOneField(Asset, on_delete=models.PROTECT)
    withdrawal_account = models.OneToOneField(Asset, null=True, on_delete=models.PROTECT, related_name='withdrawal_account')
    payment_due_day = models.IntegerField(null=True)
    payment_confirmation_day = models.IntegerField(null=True)

    def __str__(self):
        return self.asset.name
    

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