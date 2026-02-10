from django.contrib import admin
from .models import ApprovalRequest, PeriodLock
admin.site.register(ApprovalRequest)
admin.site.register(PeriodLock)
