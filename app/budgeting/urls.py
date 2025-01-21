from django.urls import path

from budgeting import views

app_name = 'budgeting'
urlpatterns = [
    path("list", views.CashflowListView.as_view(), name='cashflow_list'),
    path("<int:pk>", views.CashflowUpdateView.as_view(), name='cashflow_update'),
    path("add", views.CashflowCreateView.as_view(), name='cashflow_create'),
    path("category/", views.CashflowCategoryListView.as_view(), name='cashflow_category_list'),
    path("category/<int:pk>", views.CashflowCategoryUpdateView.as_view(), name='cashflow_category_update'),
    path("category/add", views.CashflowCategoryCreateView.as_view(), name='cashflow_category_create'),
    path("category/<int:cashflow_category_id>/mod-cashflow-category", views.mod_cashflow_category, name='mod_cashflow_category'),
    path("asset/", views.AssetListView.as_view(), name='asset_list'),
    path("asset/<int:pk>/", views.AssetDetailView.as_view(), name='asset_detail'),
    path("asset/<int:pk>/mod-asset", views.mod_asset, name='mod_asset'),
    path("asset/category/", views.AssetCategoryListView.as_view(), name='asset_category_list'),
    path("asset/category/<int:pk>/", views.AssetCategoryDetailView.as_view(), name='asset_category'),
    path("asset/category/<int:pk>/mod-asset-category", views.mod_asset_category, name='mod_asset_category'),
]