from django.contrib import admin
from core.models import  Category, Lodges, ProductImages
# Register your models here.

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class LodgesAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'title', 'lodge_Image', 'price', 'category', 'rooms', 'available', 'lid']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Lodges, LodgesAdmin)
