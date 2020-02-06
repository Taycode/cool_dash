from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    file = models.FileField(upload_to='books')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
