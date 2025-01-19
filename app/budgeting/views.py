from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, FormView, ListView

from .models import Asset, AssetCategory, CashFlow, CashFlowCategory

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


def mod_cash_flow(request, cash_flow_id):
    cash_flow = get_object_or_404(CashFlow, pk=cash_flow_id)
    
    # Modify cash flow fields.
    cash_flow.name = request.POST['name']
    cash_flow.amount = request.POST['amount']
    cash_flow.memo = request.POST['memo']

    cash_flow.save()

    return HttpResponseRedirect(reverse('budgeting:cash_flow', args=(cash_flow.id,)))


def mod_cash_flow_category(request, cash_flow_category_id):
    cash_flow_category = get_object_or_404(CashFlowCategory, pk=cash_flow_category_id)

    # Modify cash flow category fields.
    cash_flow_category.name = request.POST['name']

    cash_flow_category.save()

    return HttpResponseRedirect(reverse('budgeting:cash_flow_category', args=(cash_flow_category.id,)))


class AssetListView(ListView):
    model = Asset
    context_object_name = 'asset_list'


class AssetDetailView(DetailView):
    model = Asset
    context_object_name = 'asset'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['asset_list'] = Asset.objects.all()
        context["asset_category_list"] = AssetCategory.objects.all()
        return context


class AssetCategoryListView(ListView):
    model = AssetCategory
    context_object_name = 'asset_category_list'


class AssetCategoryDetailView(DetailView):
    model = AssetCategory
    context_object_name = 'asset_category'

class CashFlowListView(ListView):
    model = CashFlow
    template_name = 'budgeting/cash_flow_list.html'
    context_object_name = 'cash_flow_list'


class CashFlowDetaiView(DetailView):
    model = CashFlow
    template_name = 'budgeting/cash_flow_detail.html'
    context_object_name = 'cash_flow'


class CashFlowCategoryListView(ListView):
    model = CashFlowCategory
    template_name = 'budgeting/category_list.html'
    context_object_name = 'cash_flow_category_list'


class CashFlowCategoryDetailView(DetailView):
    model = CashFlowCategory
    template_name = 'budgeting/category_detail.html'
    context_object_name = 'cash_flow_category'