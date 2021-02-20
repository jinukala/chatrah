from django.urls import path, include

from . import views

urlpatterns = [
    path('tt', views.schedule, name="timetable"),
    path('credits', views.credit, name="credits")
]