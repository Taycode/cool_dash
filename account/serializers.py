from rest_framework import serializers

from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, required=True, write_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @staticmethod
    def authenticate(validated_data):
        email = validated_data['email']
        password = validated_data['password']
        try:
            user = User.objects.get(email__iexact=email)
            user = authenticate(username=user.username, password=password)
            if user is not None:
                data = {"status": "success", "token": user.auth_token.key}
                return data
        except User.DoesNotExist:
            data = {"status": "failed", "error": "Wrong credentials"}
            return data


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs = {"password": {
            "write_only": True
        }}

    def create(self, validated_data):
        user = User(
            email=validated_data["email"].lower(),
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["email"].lower()
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
