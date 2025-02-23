from django import forms

from .models import Asset, Cashflow


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            "name",
            "category",
            "amount",
            "withdrawal_account",
        ]


class CashflowForm(forms.ModelForm):
    class Meta:
        model = Cashflow
        fields = ["name", "category", "amount", "asset", "date", "memo"]
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "memo": forms.Textarea(attrs={"cols": 40, "rows": 5}),
        }
