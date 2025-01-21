from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Asset, AssetCategory, Cashflow, CashflowCategory

# Create your views here.
def mod_asset(request, pk):
    asset = get_object_or_404(Asset, pk=pk)

    # Modify asset fields.
    asset.name = request.POST['asset_name']
    asset.amount = request.POST['amount']

    asset_category = get_object_or_404(AssetCategory, pk=request.POST['category'])
    asset.category = asset_category

    if asset.category.is_credit:
        if request.POST['withdrawal_account'] != '0':
            withdrawal_account = Asset.objects.get(pk=request.POST['withdrawal_account'])
            asset.withdrawal_account = withdrawal_account
        asset.payment_due_day = request.POST['payment_due_day']
        asset.payment_confirmation_day = request.POST['payment_confirmation_day']
    else:
        asset.withdrawal_account = None
        asset.payment_due_day = None
        asset.payment_confirmation_day = None
    
    asset.save()

    return HttpResponseRedirect(reverse('budgeting:asset_detail', args=(asset.id,)))


def mod_asset_category(request, pk):
    asset_category = get_object_or_404(AssetCategory, pk=pk)

    # Modify asset category fields.
    asset_category.name = request.POST['asset_category_name']
    if 'is_credit' in request.POST:
        asset_category.is_credit = True
    else:
        asset_category.is_credit = False
    asset_category.save()

    return HttpResponseRedirect(reverse('budgeting:asset_category', args=(asset_category.id,)))


def mod_cashflow_category(request, cashflow_category_id):
    cashflow_category = get_object_or_404(CashflowCategory, pk=cashflow_category_id)

    # Modify cash flow category fields.
    cashflow_category.name = request.POST['name']

    cashflow_category.save()

    return HttpResponseRedirect(reverse('budgeting:cashflow_category', args=(cashflow_category.id,)))


class AssetListView(ListView):
    model = Asset
    context_object_name = 'asset_list'


class AssetDetailView(DetailView):
    model = Asset
    context_object_name = 'asset'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['asset_list'] = Asset.objects.all()
        context['asset_category_list'] = AssetCategory.objects.all()
        return context


class AssetCategoryListView(ListView):
    model = AssetCategory
    context_object_name = 'asset_category_list'


class AssetCategoryDetailView(DetailView):
    model = AssetCategory
    context_object_name = 'asset_category'

class CashflowListView(ListView):
    model = Cashflow
    context_object_name = 'cashflow_list'


class CashflowUpdateView(UpdateView):
    model = Cashflow
    template_name = 'budgeting/Cashflow_update_form.html'
    fields = ['name', 'category', 'amount', 'asset', 'date', 'memo']
    
    def form_valid(self, form):
        return super().form_valid(form)


class CashflowCreateView(CreateView):
    model = Cashflow
    fields = ['name', 'category', 'amount', 'asset', 'date', 'memo']

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