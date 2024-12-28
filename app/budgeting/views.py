from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Asset, AssetCategory

# Create your views here.
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