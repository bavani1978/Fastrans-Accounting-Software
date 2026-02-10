import json
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from ledger.models import Customer, Supplier, ChartOfAccount

class Command(BaseCommand):
    help = "Load demo UI data (assets/data/demo_data.json) into DB (customers/suppliers + sample COA)."

    def handle(self, *args, **kwargs):
        p = Path(settings.BASE_DIR) / "ui" / "assets" / "data" / "demo_data.json"
        if not p.exists():
            self.stdout.write(self.style.ERROR(f"Not found: {p}. Copy UI folder into backend/ui/ first."))
            return
        d = json.loads(p.read_text(encoding="utf-8"))
        for name in d.get("customers", []):
            Customer.objects.get_or_create(name=name)
        for name in d.get("suppliers", []):
            Supplier.objects.get_or_create(name=name)
        sample = [
            ("1000","Cash at Bank","ASSET"),
            ("1100","Accounts Receivable","ASSET"),
            ("2000","Accounts Payable","LIABILITY"),
            ("2100","GST Control","LIABILITY"),
            ("3000","Retained Earnings","EQUITY"),
            ("4000","Service Revenue","INCOME"),
            ("5000","Cost of Services","EXPENSE"),
            ("6100","Admin Expenses","EXPENSE"),
        ]
        for code,name,typ in sample:
            ChartOfAccount.objects.get_or_create(code=code, defaults={"name":name,"type":typ})
        self.stdout.write(self.style.SUCCESS("Loaded demo customers/suppliers/COA."))
