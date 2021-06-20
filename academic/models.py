from django.db import models

years = [
    (1,"I"),
    (2,"II"),
    (3, "III"),
    (4, "IV"),
    ]
sections = [
        (1, "A"),
        (2, "B"),
        (3, "C"),
    ]
depts = [
        (1, "CSE"),
        (2, "CIVIL"),
        (3, "EEE"),
        (4, "IT"),
        (5, "ECE"),
        (6, "MECH"),
        (7, "EIE"),
    ]

class timetables(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="TimeTable")
    year = models.IntegerField(choices=years, default=1)
    dept = models.IntegerField(choices=depts, default=1)
    section = models.IntegerField(choices=sections, default=1)
    timetable = models.ImageField(upload_to='timetable/')

    def __str__(self):
        return self.title
    

class credits(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="Credit")
    year = models.IntegerField(choices=years, default=1)
    dept = models.IntegerField(choices=depts, default=1)
    sub = models.CharField(max_length=50, unique=True)
    credit = models.IntegerField()

    def __str__(self):
        return self.title
    