from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


def create_token(sender, **kwargs):
    if kwargs['created']:
        Token.objects.create(user=kwargs['instance'])


post_save.connect(create_token, User)
