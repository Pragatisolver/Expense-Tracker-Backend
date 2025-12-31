from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("title", "amount", "category", "date", "user")


admin.site.site_header = "Trackerrr Admin Page"
admin.site.site_title = "Admin Page"
admin.site.index_title = "Welcome to Trackerrr Admin"
