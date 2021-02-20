from django.shortcuts import render
from .models import notify
from users.models import students
from django.contrib.auth import get_user
from django.views import generic
import mimetypes
from django.contrib.auth.decorators import login_required
import datetime
from django.utils.safestring import mark_safe

@login_required
def notifications(request):
    # userid = get_user(request)
    updates = notify.objects.filter(year=5).filter(dept=8).filter(section=4).order_by('time')
    dash = dict()
    for query in updates:
        dash[query.title] = [query.title, mark_safe(query.content), query.time]
    return render(request, "dashboard.html", {'dash': dash})

@login_required
def classupdates(request):
    userid = get_user(request)
    cat = students.objects.get(number=userid)
    updates = notify.objects.filter(year=cat.year).filter(dept=cat.dept).filter(section=cat.section).order_by('time')
    dash = dict()
    for query in updates:
        dash[query.title] = [query.title, mark_safe(query.content), query.time]
    return render(request, "classupdates.html", {'dash': dash})


