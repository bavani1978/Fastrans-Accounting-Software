import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Customer, Supplier, ChartOfAccount, JournalEntry, JournalLine

def _json(request):
    try: return json.loads(request.body.decode("utf-8") or "{}")
    except Exception: return {}

@login_required
@require_http_methods(["GET","POST"])
def customers(request):
    if request.method == "POST":
        p = _json(request)
        obj = Customer.objects.create(
            name=p.get("name","").strip(),
            short_code=p.get("short_code","").strip(),
            gst_applicable=bool(p.get("gst_applicable", True)),
            billing_currency=p.get("billing_currency","SGD"),
            attention=p.get("attention",""),
            contact=p.get("contact",""),
            address=p.get("address",""),
            uen=p.get("uen",""),
            gst_reg_no=p.get("gst_reg_no",""),
        )
        return JsonResponse({"ok": True, "id": obj.id})
    items = list(Customer.objects.values("id","name","short_code","gst_applicable","billing_currency"))
    return JsonResponse({"items": items})

@login_required
@require_http_methods(["GET","POST"])
def suppliers(request):
    if request.method == "POST":
        p = _json(request)
        obj = Supplier.objects.create(
            name=p.get("name","").strip(),
            contact=p.get("contact",""),
            email=p.get("email",""),
            address=p.get("address",""),
        )
        return JsonResponse({"ok": True, "id": obj.id})
    items = list(Supplier.objects.values("id","name","email"))
    return JsonResponse({"items": items})

@login_required
@require_http_methods(["GET","POST"])
def coa(request):
    if request.method == "POST":
        p = _json(request)
        obj, created = ChartOfAccount.objects.get_or_create(
            code=p.get("code","").strip(),
            defaults={"name": p.get("name","").strip(), "type": p.get("type","ASSET")}
        )
        if not created:
            obj.name = p.get("name", obj.name)
            obj.type = p.get("type", obj.type)
            obj.save()
        return JsonResponse({"ok": True, "id": obj.id})
    items = list(ChartOfAccount.objects.values("code","name","type","is_active").order_by("code"))
    return JsonResponse({"items": items})

@login_required
def gl_account(request, code: str):
    rows = JournalLine.objects.filter(account__code=code, journal__posted=True).select_related("journal")        .order_by("-journal__date")[:200]
    items = [{
        "date": r.journal.date.isoformat(),
        "entry_no": r.journal.entry_no,
        "memo": r.journal.memo,
        "debit": float(r.debit),
        "credit": float(r.credit),
        "description": r.description,
    } for r in rows]
    return JsonResponse({"account_code": code, "items": items})

@login_required
def journal_detail(request, entry_no: str):
    j = JournalEntry.objects.prefetch_related("lines__account").get(entry_no=entry_no)
    lines = [{
        "account": l.account.code,
        "account_name": l.account.name,
        "description": l.description,
        "debit": float(l.debit),
        "credit": float(l.credit),
        "gst_code": l.gst_code,
    } for l in j.lines.all()]
    return JsonResponse({"entry_no": j.entry_no, "date": j.date.isoformat(), "memo": j.memo, "posted": j.posted, "currency": j.currency, "lines": lines})
