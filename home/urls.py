from .views import *
from django.urls import path


urlpatterns = [
        path('', HomeView.as_view(), name='home'),
        path('contact', contact, name='contact'),
        path('details/<slug>', ProductDetailView.as_view(), name = 'details'),
        path('product_review/<slug>', product_review, name='product_review'),
]