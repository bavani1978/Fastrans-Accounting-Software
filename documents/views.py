from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from ledger.models import Document

@login_required
@require_http_methods(["POST"])
def upload(request):
    f = request.FILES.get("file")
    kind = request.POST.get("kind","OTHER")
    if not f:
        return JsonResponse({"ok": False, "error": "No file"}, status=400)
    doc = Document.objects.create(kind=kind, filename=f.name, file=f, uploaded_by=request.user)
    return JsonResponse({"ok": True, "id": doc.id, "filename": doc.filename})

@login_required
def list_docs(request):
    items = list(Document.objects.order_by("-created_at").values("id","kind","filename","status","created_at")[:200])
    return JsonResponse({"items": items})
