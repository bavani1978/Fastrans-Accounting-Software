from django.contrib import admin
from .models import ChartOfAccount, Customer, Supplier, Document, JournalEntry, JournalLine

@admin.register(ChartOfAccount)
class COAAdmin(admin.ModelAdmin):
    list_display = ("code","name","type","is_active")
    search_fields = ("code","name")

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name","short_code","gst_applicable","billing_currency")
    search_fields = ("name","short_code")

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name","email")
    search_fields = ("name","email")

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id","kind","filename","status","created_at")
    search_fields = ("filename",)

class JournalLineInline(admin.TabularInline):
    model = JournalLine
    extra = 0

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ("entry_no","date","memo","posted","currency")
    search_fields = ("entry_no","memo")
    inlines = [JournalLineInline]
