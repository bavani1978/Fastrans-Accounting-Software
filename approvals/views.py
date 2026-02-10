import json
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import ApprovalRequest, PeriodLock

def _json(request):
    try: return json.loads(request.body.decode("utf-8") or "{}")
    except Exception: return {}

@login_required
def queue(request):
    items = list(ApprovalRequest.objects.filter(status="PENDING").order_by("-created_at").values(
        "id","request_type","object_ref","summary","created_at"
    ))
    return JsonResponse({"items": items})

@login_required
@require_http_methods(["POST"])
def approve(request, pk: int):
    p = _json(request)
    ar = ApprovalRequest.objects.get(pk=pk)
    ar.status = "APPROVED"
    ar.approved_by = request.user
    ar.approved_at = timezone.now()
    ar.comments = p.get("comments","")
    ar.save()
    return JsonResponse({"ok": True, "id": ar.id})

@login_required
@require_http_methods(["POST"])
def reject(request, pk: int):
    p = _json(request)
    ar = ApprovalRequest.objects.get(pk=pk)
    ar.status = "REJECTED"
    ar.approved_by = request.user
    ar.approved_at = timezone.now()
    ar.comments = p.get("comments","")
    ar.save()
    return JsonResponse({"ok": True, "id": ar.id})

@login_required
@require_http_methods(["POST"])
def period_lock_request(request):
    p = _json(request)
    fy = int(p.get("fiscal_year"))
    period = int(p.get("period"))
    obj, _ = PeriodLock.objects.get_or_create(fiscal_year=fy, period=period)
    obj.status = "LOCK_REQUESTED"
    obj.requested_by = request.user
    obj.requested_at = timezone.now()
    obj.comments = p.get("comments","")
    obj.save()
    ApprovalRequest.objects.create(
        request_type="PERIOD_LOCK",
        object_ref=f"PERIOD:{fy}-{period:02d}",
        summary=f"Request lock FY{fy} period {period:02d}",
        requested_by=request.user,
    )
    return JsonResponse({"ok": True})

@login_required
def period_lock_status(request):
    fy = int(request.GET.get("fiscal_year","2026"))
    period = int(request.GET.get("period","1"))
    obj, _ = PeriodLock.objects.get_or_create(fiscal_year=fy, period=period)
    return JsonResponse({"fiscal_year": fy, "period": period, "status": obj.status})

@login_required
def approval_audit_report(request):
    rows = ApprovalRequest.objects.order_by("-created_at")[:500]
    items = [{
        "id": r.id,
        "request_type": r.request_type,
        "object_ref": r.object_ref,
        "summary": r.summary,
        "status": r.status,
        "requested_by": getattr(r.requested_by,"username",None),
        "approved_by": getattr(r.approved_by,"username",None),
        "approved_at": r.approved_at.isoformat() if r.approved_at else None,
        "comments": r.comments,
    } for r in rows]
    return JsonResponse({"items": items})
