# Generated by Django 3.0.3 on 2020-02-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_course_outline'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
