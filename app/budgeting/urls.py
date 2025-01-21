from django.urls import path

from budgeting import views

app_name = 'budgeting'
urlpatterns = [
    path("list", views.CashflowListView.as_view(), name='cashflow_list'),
    path("<int:pk>", views.CashflowUpdateView.as_view(), name='cashflow_update'),
    path("create", views.CashflowCreateView.as_view(), name='cashflow_create'),
    path("category/", views.CashflowCategoryListView.as_view(), name='cashflow_category_list'),
    path("category/<int:pk>", views.CashflowCategoryUpdateView.as_view(), name='cashflow_category_update'),
    path("category/create", views.CashflowCategoryCreateView.as_view(), name='cashflow_category_create'),
    path("asset/", views.AssetListView.as_view(), name='asset_list'),
    path("asset/<int:pk>/", views.AssetUpdateView.as_view(), name='asset_update'),
    path("asset/create", views.AssetCreateView.as_view(), name='asset_create'),
    path("asset/category/", views.AssetCategoryListView.as_view(), name='asset_category_list'),
    path("asset/category/<int:pk>/", views.AssetCategoryUpdateView.as_view(), name='asset_category_update'),
    path("asset/category/create", views.AssetCategoryCreateView.as_view(), name='asset_category_create'),
]