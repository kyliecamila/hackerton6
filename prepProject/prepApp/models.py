from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1, related_name="subjects")
    subject = models.CharField(max_length=255)
    professor = models.CharField(max_length=255)
    day1 = models.CharField(max_length=3, blank=True)
    day2 = models.CharField(max_length=3, blank=True)
    start_time = models.TimeField(blank=True, null=True)
    finish_time = models.TimeField(blank=True, null=True)
    # RECORD_CHOICES = (
    #     ('zoom','zoom'),
    #     ('collaborate','collaborate')
    # )
    record_choices = models.CharField(max_length=255)
    # def __str__(self):
    #     self.subject

class Recordings(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)
    date = models.DateField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, related_name = 'recording')
    record = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    

    # def __str__(self):
    #     str(self.subject)
