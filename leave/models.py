from django.db import models
from users.models import students

# Create your models here.
class leave(models.Model):
    STATUS = (
    (0,"Applied"),
    (1,"Accepted"),
    (2, "Rejected")
    )
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
    title =models.CharField(max_length=200, unique=True)
    number = models.CharField(max_length=15, unique=True, primary_key=True, default="000000000")
    year = models.IntegerField(choices=years, default=1)
    dept = models.IntegerField(choices=depts, default=1)
    section = models.IntegerField(choices=sections, default=1)
    created_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.number
    