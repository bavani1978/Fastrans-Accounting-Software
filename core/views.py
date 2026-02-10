import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

def health(request):
    return JsonResponse({"ok": True, "service": "fastrans_backend"})

def me(request):
    u = request.user
    if not u.is_authenticated:
        return JsonResponse({"authenticated": False}, status=401)
    return JsonResponse({"authenticated": True, "username": u.username, "is_staff": u.is_staff})

@csrf_exempt  # demo only
@require_http_methods(["POST"])
def login_view(request):
    try:
        payload = json.loads(request.body.decode("utf-8") or "{}")
    except Exception:
        payload = {}
    user = authenticate(request, username=payload.get("username",""), password=payload.get("password",""))
    if user is None:
        return JsonResponse({"ok": False, "error": "Invalid credentials"}, status=401)
    login(request, user)
    return JsonResponse({"ok": True, "username": user.username})

@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return JsonResponse({"ok": True})
