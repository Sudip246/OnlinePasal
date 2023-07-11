from django.urls import path, include
from rest_framework import routers
from .api_views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'brand', BrandViewSet)
router.register(r'ad', AdViewSet)
router.register(r'slider', SliderViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('product_filter', ProductListView.as_view(), name = "product_filter"),
    path('product_crud/<int:pk>',ProductDetailView.as_view(), name="product_crud"),

    path('category_filter', CategoryListView.as_view(), name = "category_filter"),
    path('category_crud/<int:pk>',CategoryDetailView.as_view(), name="category_crud"),

    path('brand_filter', BrandListView.as_view(), name = "brand_filter"),
    path('brand_crud/<int:pk>',BrandDetailView.as_view(), name="brand_crud"),

    path('ad_filter', AdListView.as_view(), name = "ad_filter"),
    path('ad_crud/<int:pk>',AdDetailView.as_view(), name="ad_crud"),

    path('slider_filter', SliderListView.as_view(), name="slider_filter"),
    path('slider_crud/<int:pk>', SliderDetailView.as_view(), name="slider_crud"),

]