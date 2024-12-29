from django.urls import path

from . import views

app_name = 'budgeting'
urlpatterns = [
    path("", views.CashFlowListView.as_view(), name='cash_flow_list'),
    path("<int:pk>", views.CashFlowDetaiView.as_view(), name='cash_flow'),
    path("category/", views.CashFlowCategoryListView.as_view(), name='cash_flow_category_list'),
    path("category/<int:pk>", views.CashFlowCategoryDetailView.as_view(), name='cash_flow_category'),
    path("asset/", views.AssetListView.as_view(), name='asset_list'),
    path("asset/<int:pk>/", views.AssetDetailView.as_view(), name='asset_detail'),
    path("asset/<int:asset_id>/mod-asset", views.mod_asset, name='mod_asset'),
    path("asset-category/", views.AssetCategoryListView.as_view(), name='asset_category_list'),
    path("asset-category/<int:pk>/", views.AssetCategoryDetailView.as_view(), name='asset_category'),
    path("asset-category/<int:asset_category_id>/mod-asset-category", views.mod_asset_category, name='mod_asset_category'),
]