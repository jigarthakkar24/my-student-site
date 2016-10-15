from django.db import models
from django.utils import timezone


class Student(models.Model):
    author = models.ForeignKey('auth.User')
    trainer = models.CharField(max_length=200)
    placement_student_name = models.CharField(max_length=200)
    remarks = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.trainer
