from django.urls import path

from . import views

urlpatterns = [
    path("apply", views.apply_leave, name="apply"),
    path("status", views.leave_status, name="status")
]