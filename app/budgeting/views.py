from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView

from .forms import CashflowForm
from .models import Asset, AssetCategory, Cashflow, CashflowCategory

# Create your views here.
class AssetListView(ListView):
    model = Asset


class AssetUpdateView(UpdateView):
    model = Asset
    fields = ['name', 'category', 'amount', 'withdrawal_account', 'payment_due_day', 'payment_confirmation_day']


class AssetCreateView(CreateView):
    model = Asset
    fields = ['name', 'category', 'amount', 'withdrawal_account', 'payment_due_day', 'payment_confirmation_day']


class AssetCategoryListView(ListView):
    model = AssetCategory
    context_object_name = 'asset_category_list'


class AssetCategoryUpdateView(UpdateView):
    model = AssetCategory
    fields = ['name', 'is_credit']


class AssetCategoryCreateView(CreateView):
    model = AssetCategory
    fields = ['name', 'is_credit']


class CashflowListView(ListView):
    model = Cashflow
    context_object_name = 'cashflow_list'


class CashflowUpdateView(UpdateView):
    model = Cashflow
    form_class = CashflowForm
    # fields = ['name', 'category', 'amount', 'asset', 'date', 'memo']
    
    def form_valid(self, form):
        return super().form_valid(form)


class CashflowCreateView(CreateView):
    model = Cashflow
    form_class = CashflowForm
    # fields = ['name', 'category', 'amount', 'asset', 'date', 'memo']

    def form_valid(self, form):
        category = CashflowCategory.objects.get(pk=self.request.POST['category'])
        asset = Asset.objects.get(pk=self.request.POST['asset'])

        if category.is_income:
            asset.amount += int(self.request.POST['amount'])
        else:
            asset.amount -= int(self.request.POST['amount'])
        asset.save()
        
        return super().form_valid(form)


class CashflowCategoryListView(ListView):
    model = CashflowCategory
    context_object_name = 'cashflow_category_list'


class CashflowCategoryUpdateView(UpdateView):
    model = CashflowCategory
    fields = ['name']


class CashflowCategoryCreateView(CreateView):
    model = CashflowCategory
    fields = ['name', 'is_income']