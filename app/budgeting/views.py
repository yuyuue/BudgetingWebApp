from django.shortcuts import render
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


class AssetCategoryListView(generic.ListView):
    model = AssetCategory
    template_name = 'asset/cat_list.html'
    context_object_name = 'asset_category_list'


class AssetCategoryDetailView(generic.DetailView):
    model = AssetCategory
    template_name = 'asset/cat_detail.html'