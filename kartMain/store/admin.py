from django.contrib import admin
from .models import Product,Variation,ReviewRating,ProductGallery
# Register your models here.
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)