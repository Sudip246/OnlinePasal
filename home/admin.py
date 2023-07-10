from django.contrib import admin
from .models import *

# Register your models here.




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("image", "slug", )
    search_fields = ("name", "slug")


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("name","description")
    list_filter = ("image", "url", )
    search_fields = ("name", "url")


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_filter = ("image",)
    search_fields = ("name", "image")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("image", "slug",)
    search_fields = ("name", "slug")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", 'email', 'message')
    list_filter = ("name", "subject", )
    search_fields = ("email", "name")


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('address', "email")
    list_filter = ("phone", "email", )
    search_fields = ("email", "address")


@admin.register(ProductImages)
class Admin(admin.ModelAdmin):
    list_display = ("name","image")
    list_filter = ("image", "product",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "brand", "labels")
    list_filter = ("category", "labels", "status")
    search_fields = ("name", "description")


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ("name", 'email', "comment", "star")
    list_filter = ("name", "email", "date")
    search_fields = ("name", "slug")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("username", "slug", "quantity","total", "checkout")
    list_filter = ("checkout", "date")
    search_fields = ("username", "slug")


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ("username", "slug", "date", "items",)
    list_filter = ("username", "items")
    search_fields = ("username", "slug")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("fname", 'lname', "email", "phone", "address", )
    list_filter = ("email", "phone", "country", "city", "state")
    search_fields =("email", "phone", "city")
