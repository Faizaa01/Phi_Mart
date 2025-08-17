from product.models import Product, Category, Review, ProductImage
from django.contrib import admin


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Review)
