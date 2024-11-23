from django.contrib import admin
from .models import Celestial, Category, ImageCelestial


class ImageCelestialInline(admin.TabularInline):
    model = ImageCelestial
    extra = 3


@admin.register(Celestial)
class CelestialAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated',
                    'discount']
    list_editable = ['price', 'available', 'discount']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['name', 'slug']
    list_filter = ['available', 'created', 'updated']
    list_per_page = 5
    inlines = [ImageCelestialInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}