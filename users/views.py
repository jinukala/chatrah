from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import students
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "welcome.html")
    
def signup(request):
    if request.method == "GET":
        return render(request, "register.html", context=None)
    _name = request.POST["name"]
    _number = request.POST["number"]
    _yoa = request.POST["yoa"]
    _year = request.POST["year"]
    _dept = request.POST["dept"]
    _section = request.POST["section"]
    _password = request.POST["pwd"]
    _rpassword = request.POST["rpwd"]
    if _password != _rpassword:
        return HttpResponse("Password match Failed")
    join = students(name=_name, number=_number, YoA=_yoa, year=_year, dept=_dept, section=_section)
    join.save()
    user = User.objects.create_user(_number,"NULL", _password)
    return redirect("/login")


def loginstudent(request):
    if request.method == "GET":
        return render(request, "login.html", context=None)
    _number = request.POST["number"]
    _dept = request.POST["dept"]
    _password = request.POST["pwd"]
    user = authenticate(request, username=_number, password=_password)
    if user is not None:
        login(request, user)
        return redirect("/profile")
    else:
        return HttpResponse("error")

@login_required
def profile(request):
    userid = get_user(request)
    #user = students.objects.raw("SELECT name, number, YoA, year, dept, section FROM users_students WHERE number=%s", [userid])
    user = students.objects.get(number=userid)
    years = {1:"I",2:"II",3: "III",4: "IV"}
    sections = {1: "A",2: "B",3: "C"}
    depts = {1: "CSE",2: "CIVIL",3: "EEE",4: "IT",5: "ECE",6: "MECH",7: "EIE"}
    return render(request, "profile.html", context={"name": user.name, "number": user.number, "YoA": user.YoA, "year": years[user.year], "dept": depts[user.dept],"section": sections[user.section]})
    
@login_required
def logoutstudent(request):
    logout(request)
    return redirect("/login")

