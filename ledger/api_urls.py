from django.urls import path
from . import views
urlpatterns = [
    path("customers/", views.customers),
    path("suppliers/", views.suppliers),
    path("coa/", views.coa),
    path("gl/<str:code>/", views.gl_account),
    path("journals/<str:entry_no>/", views.journal_detail),
]
