from django.shortcuts import render
from .models import timetables, credits
from users.models import students
from django.contrib.auth import get_user
from django.views import generic
import mimetypes
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def schedule(request):
    userid = get_user(request)
    cat = students.objects.get(number=userid)
    updates = timetables.objects.filter(year=cat.year).filter(dept=cat.dept).filter(section=cat.section)
    dash = dict()
    for query in updates:
        dash[query.title] = query.timetable
    return render(request, "timetable.html", {'dash': dash})

@login_required
def credit(request):
    userid = get_user(request)
    cat = students.objects.get(number=userid)
    updates = credits.objects.filter(year=cat.year).filter(dept=cat.dept)
    dash = dict()
    for query in updates:
        dash[query.sub] = query.credit
    print(dash)
    return render(request, "credits.html", {'dash': dash})
