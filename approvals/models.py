from django.db import models

class ApprovalRequest(models.Model):
    STATUS = [("PENDING","Pending"),("APPROVED","Approved"),("REJECTED","Rejected")]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    request_type = models.CharField(max_length=40)
    object_ref = models.CharField(max_length=80)
    summary = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=20, choices=STATUS, default="PENDING")
    requested_by = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.SET_NULL, related_name="approval_requested")
    approved_by = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.SET_NULL, related_name="approval_approved")
    approved_at = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(blank=True, default="")

class PeriodLock(models.Model):
    STATUS = [("OPEN","Open"),("LOCK_REQUESTED","Lock requested"),("LOCKED","Locked")]
    fiscal_year = models.IntegerField()
    period = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default="OPEN")
    requested_by = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.SET_NULL, related_name="periodlock_requested")
    approved_by = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.SET_NULL, related_name="periodlock_approved")
    requested_at = models.DateTimeField(null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(blank=True, default="")
    class Meta:
        unique_together = ("fiscal_year","period")
