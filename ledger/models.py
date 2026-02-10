from django.db import models
from django.conf import settings

class Timestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class ChartOfAccount(Timestamped):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=30, choices=[
        ("ASSET","Asset"),("LIABILITY","Liability"),("EQUITY","Equity"),
        ("INCOME","Income"),("EXPENSE","Expense")
    ])
    is_active = models.BooleanField(default=True)
    def __str__(self): return f"{self.code} {self.name}"

class Customer(Timestamped):
    name = models.CharField(max_length=255, unique=True)
    short_code = models.CharField(max_length=20, blank=True, default="")
    gst_applicable = models.BooleanField(default=True)
    billing_currency = models.CharField(max_length=10, default=getattr(settings,"FUNCTIONAL_CURRENCY","SGD"))
    attention = models.CharField(max_length=255, blank=True, default="")
    contact = models.CharField(max_length=255, blank=True, default="")
    address = models.TextField(blank=True, default="")
    uen = models.CharField(max_length=30, blank=True, default="")
    gst_reg_no = models.CharField(max_length=30, blank=True, default="")
    def __str__(self): return self.name

class Supplier(Timestamped):
    name = models.CharField(max_length=255, unique=True)
    contact = models.CharField(max_length=255, blank=True, default="")
    email = models.CharField(max_length=255, blank=True, default="")
    address = models.TextField(blank=True, default="")
    def __str__(self): return self.name

class Document(Timestamped):
    kind = models.CharField(max_length=30, choices=[("INVOICE","Invoice"),("BILL","Bill"),("BANK","BankStatement"),("OTHER","Other")])
    filename = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/%Y/%m/")
    status = models.CharField(max_length=20, default="UPLOADED")
    uploaded_by = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.SET_NULL)

class JournalEntry(Timestamped):
    entry_no = models.CharField(max_length=40, unique=True)
    date = models.DateField()
    memo = models.CharField(max_length=255, blank=True, default="")
    source_type = models.CharField(max_length=30, blank=True, default="")
    source_id = models.CharField(max_length=60, blank=True, default="")
    currency = models.CharField(max_length=10, default=getattr(settings,"FUNCTIONAL_CURRENCY","SGD"))
    posted = models.BooleanField(default=False)
    posted_by = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.SET_NULL, related_name="posted_journals")

class JournalLine(Timestamped):
    journal = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name="lines")
    account = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, blank=True, default="")
    debit = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, blank=True, on_delete=models.SET_NULL)
    gst_code = models.CharField(max_length=10, blank=True, default="")
