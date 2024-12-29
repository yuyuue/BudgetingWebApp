from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Asset, AssetCategory, CashFlow, CashFlowCategory

# Create your views here.
def mod_asset(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)

    # Modify asset fields.
    asset.name = request.POST['name']
    asset.amount = request.POST['amount']
    # Info relate to credit.
    if 'asset_is_credit' in request.POST:
        asset.withdrawal_account = request.POST['withdrawal_account']
        asset.payment_due_date = request.POST['payment_due_date']
        asset.payment_confirmation_date = request.POST['payment_confirmation_date']
    asset.save()
    
    return HttpResponseRedirect(reverse('budgeting:asset_detail', args=(asset.id,)))


def mod_asset_category(request, asset_category_id):
    asset_category = get_object_or_404(Asset, pk=asset_category_id)

    # Modify asset category fields.
    asset_category.name = request.POST['name']
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


class AssetListView(generic.ListView):
    model = Asset
    template_name = 'asset/asset_list.html'
    context_object_name = 'asset_list'


class AssetDetailView(generic.DetailView):
    model = Asset
    template_name = 'asset/asset_detail.html'
    context_object_name = 'asset'


class AssetCategoryListView(generic.ListView):
    model = AssetCategory
    template_name = 'asset/category_list.html'
    context_object_name = 'asset_category_list'


class AssetCategoryDetailView(generic.DetailView):
    model = AssetCategory
    template_name = 'asset/category_detail.html'
    context_object_name = 'asset_category'

class CashFlowListView(generic.ListView):
    model = CashFlow
    template_name = 'budgeting/cash_flow_list.html'
    context_object_name = 'cash_flow_list'


class CashFlowDetaiView(generic.DetailView):
    model = CashFlow
    template_name = 'budgeting/cash_flow_detail.html'
    context_object_name = 'cash_flow'


class CashFlowCategoryListView(generic.ListView):
    model = CashFlowCategory
    template_name = 'budgeting/category_list.html'
    context_object_name = 'cash_flow_category_list'


class CashFlowCategoryDetailView(generic.DetailView):
    model = CashFlowCategory
    template_name = 'budgeting/category_detail.html'
    context_object_name = 'cash_flow_category'