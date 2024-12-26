from django.urls import path

from . import views

app_name = 'budgeting'
urlpatterns = [
    path("asset/", views.AssetListView.as_view(), name='assetlist'),
    path("asset/<int:pk>", views.AssetDetailView.as_view(), name='assetdetail'),
    path("asset/", views.AssetCategoryListView.as_view(), name='assetcategory'),
    path("asset/", views.AssetCategoryDetailView.as_view(), name='assetcategorylist'),
]