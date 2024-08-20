from django.contrib import admin
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'status', 'in_stock', 'featured']
    search_fields = ['title', 'description']
    list_filter = ['category', 'product_status', 'status', 'featured']
    fields = ['user', 'category', 'title', 'image', 'description', 'price', 'specifications', 'tags', 'product_status', 'status', 'in_stock', 'featured', 'digital', 'sku']
    #inlines = [ProductImagesAdmin]
    #list_display = ['user', 'title', 'product_image', 'price', 'featured', 'product_status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', 'order_date', 'product_status']

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'item', 'price', 'qty', 'total']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
