from django.contrib import admin
from .models import (
    Newspaper, PrintingHouse, PostOffice, PrintingRun, Distribution
)


class PrintingRunInline(admin.TabularInline):
    model = PrintingRun
    extra = 1


class DistributionInline(admin.TabularInline):
    model = Distribution
    extra = 1


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_index', 'editor_full_name', 'price_per_copy']
    list_filter = ['price_per_copy']
    search_fields = ['title', 'publication_index', 'editor_first_name', 'editor_last_name']


@admin.register(PrintingHouse)
class PrintingHouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'address']
    inlines = [PrintingRunInline, DistributionInline]


@admin.register(PostOffice)
class PostOfficeAdmin(admin.ModelAdmin):
    list_display = ['number', 'address']
    search_fields = ['number', 'address']
    inlines = [DistributionInline]


@admin.register(PrintingRun)
class PrintingRunAdmin(admin.ModelAdmin):
    list_display = ['printing_house', 'newspaper', 'circulation']
    list_filter = ['printing_house', 'circulation']
    search_fields = ['newspaper__title', 'printing_house__name']


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ['post_office', 'newspaper', 'printing_house', 'quantity']
    list_filter = ['post_office', 'printing_house']
    search_fields = ['post_office__number', 'newspaper__title', 'printing_house__name']