from django.urls import path
from . import views
urlpatterns=[
 path('batches/',views.batches),
 path('mapping/',views.mapping),
 path('unmapped-report/',views.unmapped_report),
 path('validate-tieouts/',views.validate_tieouts),
]
