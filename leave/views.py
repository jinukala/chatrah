from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import leave
from users.models import students
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def apply_leave(request):
    userid = get_user(request)
    if request.method == "GET":
        return render(request, "apply.html")
    title = request.POST["title"]
    reason = request.POST["reason"]
    user = students.objects.get(number=userid)
    apply = leave(title=title, number=user.number, year=user.year, dept=user.dept, section=user.section, content=reason)
    apply.save()
    return redirect("/leave/status")

def leave_status(request):
    userid = get_user(request)
    STATUS = {0:"Applied",1:"Accepted",2: "Rejected"}
    leaves = leave.objects.filter(number=userid)
    if not leaves.exists():
        return render(request, "status.html", {"title": "None","date": "None", "status": "None"})
    else:
        dictl = dict()
        for query in leaves:
            dictl["title"] = query.title
            dictl["date"] = query.created_on
            dictl["status"] = STATUS[query.status]
        print(dictl)
        return render(request, "status.html", {'leave': dictl})
        
       
    
