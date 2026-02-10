from django.urls import path
from . import views
urlpatterns=[
 path('kpis/',views.kpis),
 path('revenue-by-customer/',views.revenue_by_customer),
 path('ar-ageing/',views.ar_ageing),
 path('ap-due/',views.ap_due),
 path('cashflow-forecast/',views.cashflow_forecast),
 path('gross-margin-trend/',views.gross_margin_trend),
]
