from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_code = models.CharField(max_length=6)
    course_title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    part = models.CharField(max_length=1, default=1)
    outline = models.TextField(blank=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return f'{self.course_code} - {self.course_title}'


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='books')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.title
