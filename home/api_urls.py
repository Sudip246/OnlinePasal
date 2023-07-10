from django.urls import path, include
from rest_framework import routers
from .api_views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'category', CategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('product_filter', ProductListView.as_view(), name = "product_filter"),
    path('product_crud/<int:pk>',ProductDetailView.as_view(), name="product_crud"),

    path('category_filter', CategoryListView.as_view(), name = "product_filter"),
    path('category_crud/<int:pk>',CategoryDetailView.as_view(), name="product_crud"),

]