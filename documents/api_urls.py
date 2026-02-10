from django.urls import path
from . import views
urlpatterns=[path('upload/',views.upload),path('list/',views.list_docs)]
