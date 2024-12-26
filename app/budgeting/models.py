from django.db import models

# Create your models here.
class AssetCategory(models.Model):
    pass


class Asset(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(AssetCategory, on_delete=models.PROTECT)
    amount = models.IntegerField


class Credit(models.Model):
    pass


class IncomeCategory(models.Model):
    pass


class Income(models.Model):
    pass


class ExpenceCategory(models.Model):
    pass


class Expence(models.Model):
    pass