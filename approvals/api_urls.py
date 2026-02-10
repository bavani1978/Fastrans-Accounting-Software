from django.urls import path
from . import views
urlpatterns = [
    path("queue/", views.queue),
    path("approve/<int:pk>/", views.approve),
    path("reject/<int:pk>/", views.reject),
    path("period-lock/request/", views.period_lock_request),
    path("period-lock/status/", views.period_lock_status),
    path("audit-report/", views.approval_audit_report),
]
