import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView

from .forms import AssetForm, CashflowForm
from .models import (
    Asset,
    AssetCategory,
    Cashflow,
    CashflowCategory,
    CashflowSubCategory,
)


# Create your views here.
def index(request):
    return render(request, "budgeting/index.html")


def approve(request):
    asset = Asset.objects.get(pk=request.POST["asset_id"])
    tmp = asset.amount
    asset.amount = 0
    asset.save()

    asset = asset.withdrawal_account
    asset.amount += tmp
    asset.save()

    return redirect("/budgeting/asset")


class AssetListView(ListView):
    model = Asset


class AssetUpdateView(UpdateView):
    model = Asset
    form_class = AssetForm


class AssetCreateView(CreateView):
    model = Asset
    form_class = AssetForm


class AssetCategoryListView(ListView):
    model = AssetCategory
    context_object_name = "asset_category_list"


class AssetCategoryUpdateView(UpdateView):
    model = AssetCategory
    fields = ["name", "is_credit"]


class AssetCategoryCreateView(CreateView):
    model = AssetCategory
    fields = ["name", "is_credit"]


class CashflowListView(ListView):
    model = Cashflow
    context_object_name = "cashflow_list"


class CashflowUpdateView(UpdateView):
    model = Cashflow
    form_class = CashflowForm

    def form_valid(self, form):
        return super().form_valid(form)


class CashflowCreateView(CreateView):
    model = Cashflow
    form_class = CashflowForm

    def form_valid(self, form):
        sub_category = CashflowSubCategory.objects.get(pk=self.request.POST["category"])
        asset = Asset.objects.get(pk=self.request.POST["asset"])

        if sub_category.parent_category.is_income:
            # 収入の場合
            asset.amount += int(self.request.POST["amount"])
        else:
            # 支出の場合
            # 予算超過の場合はリダイレクト
            if asset.amount < int(self.request.POST["amount"]) and not asset.category.is_credit:
                return HttpResponseRedirect("/budgeting/cashflow")
            asset.amount -= int(self.request.POST["amount"])
        asset.save()

        return super().form_valid(form)


class CashflowCategoryListView(ListView):
    model = CashflowSubCategory
    template_name = "budgeting/cashFlowCategory_list.html"
    context_object_name = "cashflow_category_list"


class CashflowCategoryUpdateView(UpdateView):
    model = CashflowCategory
    fields = ["name"]


class CashflowCategoryCreateView(CreateView):
    model = CashflowCategory
    fields = ["name", "is_income"]
