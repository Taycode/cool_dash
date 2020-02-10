from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserCreateSerializer, LoginSerializer

from django.contrib.auth.models import User


class SignUpView(APIView):

    serializer_class = UserCreateSerializer

    @staticmethod
    def post(request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["email"]

            try:

                User.objects.get(username=username)
                data = {"error": "User already exists"}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            except User.DoesNotExist:

                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    serializer_class = LoginSerializer

    @staticmethod
    def post(request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.authenticate(request.data)
            if data['status'] == 'success':
                return Response(data, status=status.HTTP_200_OK)
            elif data['status'] == 'failed':
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
