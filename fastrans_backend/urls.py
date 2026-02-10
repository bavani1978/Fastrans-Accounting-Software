from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.api_urls")),
    path("api/ledger/", include("ledger.api_urls")),
    path("api/approvals/", include("approvals.api_urls")),
    path("api/imports/", include("imports.api_urls")),
    path("api/cfo/", include("cfo.api_urls")),
    path("api/documents/", include("documents.api_urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
