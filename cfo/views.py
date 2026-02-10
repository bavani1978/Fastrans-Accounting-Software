import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings

def _load_demo():
    from pathlib import Path
    p = Path(settings.BASE_DIR) / "ui" / "assets" / "data" / "demo_data.json"
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))

@login_required
def kpis(request):
    d = _load_demo()
    if not d:
        return JsonResponse({"functional_currency": getattr(settings,"FUNCTIONAL_CURRENCY","SGD"), "kpis": {}})
    return JsonResponse({"functional_currency": d.get("meta",{}).get("functional_currency","SGD"), "as_of": d.get("meta",{}).get("as_of"), "kpis": d.get("kpis",{})})

@login_required
def revenue_by_customer(request):
    d = _load_demo()
    if not d:
        return JsonResponse({"items":[]})
    m = {}
    for inv in d.get("ar_open_invoices", []):
        m[inv["customer"]] = m.get(inv["customer"], 0) + float(inv.get("amount_sgd", 0))
    items = [{"customer": k, "revenue_sgd": v} for k,v in sorted(m.items(), key=lambda x: -x[1])]
    return JsonResponse({"items": items, "currency":"SGD"})

@login_required
def ar_ageing(request):
    d = _load_demo()
    if not d:
        return JsonResponse({"items":[]})
    return JsonResponse({"as_of": d.get("meta",{}).get("as_of"), "items": d.get("ar_open_invoices", []), "currency":"SGD"})

@login_required
def ap_due(request):
    d = _load_demo()
    if not d:
        return JsonResponse({"items":[]})
    return JsonResponse({"as_of": d.get("meta",{}).get("as_of"), "items": d.get("ap_open_bills", []), "currency":"SGD"})

@login_required
def cashflow_forecast(request):
    d = _load_demo()
    if not d:
        return JsonResponse({"items":[]})
    return JsonResponse({"as_of": d.get("meta",{}).get("as_of"), "items": d.get("cashflow_12w", []), "currency":"SGD"})

@login_required
def gross_margin_trend(request):
    d = _load_demo()
    if not d:
        return JsonResponse({"items":[]})
    return JsonResponse({"items": d.get("gross_profit_trend", []), "currency":"SGD"})
