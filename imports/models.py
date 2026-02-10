from django.db import models

class ImportBatch(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=40, default="TRANSACTIONS")
    status = models.CharField(max_length=20, default="PENDING")
    uploaded_file = models.FileField(upload_to="imports/%Y/%m/", null=True, blank=True)
    validation_report = models.JSONField(default=dict, blank=True)

class COAMapping(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    old_code = models.CharField(max_length=40)
    old_desc = models.CharField(max_length=255, blank=True, default="")
    new_code = models.CharField(max_length=40)  # many-to-one allowed
    note = models.CharField(max_length=255, blank=True, default="")
    class Meta:
        unique_together = ("old_code","new_code")
