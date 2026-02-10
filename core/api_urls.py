from django.urls import path
from . import views
urlpatterns = [
    path("health/", views.health),
    path("session/me/", views.me),
    path("auth/login/", views.login_view),
    path("auth/logout/", views.logout_view),
]
