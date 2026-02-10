import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import ImportBatch, COAMapping

def _json(request):
    try: return json.loads(request.body.decode("utf-8") or "{}")
    except Exception: return {}

@login_required
@require_http_methods(["GET","POST"])
def batches(request):
    if request.method == "POST":
        p = _json(request)
        b = ImportBatch.objects.create(name=p.get("name","Batch"), kind=p.get("kind","TRANSACTIONS"))
        return JsonResponse({"ok": True, "id": b.id})
    items = list(ImportBatch.objects.order_by("-created_at").values("id","name","kind","status","created_at","validation_report")[:200])
    return JsonResponse({"items": items})

@login_required
@require_http_methods(["GET","POST"])
def mapping(request):
    if request.method == "POST":
        p = _json(request)
        obj, _ = COAMapping.objects.get_or_create(old_code=p.get("old_code","").strip(), new_code=p.get("new_code","").strip())
        obj.old_desc = p.get("old_desc","")
        obj.note = p.get("note","")
        obj.save()
        return JsonResponse({"ok": True, "id": obj.id})
    items = list(COAMapping.objects.values("id","old_code","old_desc","new_code","note").order_by("old_code")[:500])
    return JsonResponse({"items": items})

@login_required
def unmapped_report(request):
    old_codes = request.GET.get("old_codes","")
    codes = [c.strip() for c in old_codes.split(",") if c.strip()]
    mapped = set(COAMapping.objects.filter(old_code__in=codes).values_list("old_code", flat=True))
    unmapped = [c for c in codes if c not in mapped]
    return JsonResponse({"unmapped_old_codes": unmapped, "count": len(unmapped)})

@login_required
def validate_tieouts(request):
    return JsonResponse({
        "status": "stub",
        "checks": [
            {"name":"Trial Balance agrees", "status":"PENDING"},
            {"name":"AR ageing ties to control", "status":"PENDING"},
            {"name":"AP ageing ties to control", "status":"PENDING"},
            {"name":"GST control ties to Form 5", "status":"PENDING"},
        ]
    })
