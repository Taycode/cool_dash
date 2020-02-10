from django.contrib import admin

from .models import Book, Department, Faculty, Course


admin.site.register(Book)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Course)
