from django.contrib import admin
from .models import Status, OperationType, Category, Subcategory, Transaction


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["name", "order"]


@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "order"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "operation_type", "order"]
    list_filter = ["operation_type"]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "order"]
    list_filter = ["category__operation_type", "category"]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["date", "status", "operation_type", "category", "subcategory", "amount"]
    list_filter = ["status", "operation_type", "category"]
    date_hierarchy = "date"
