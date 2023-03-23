from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from .tests import BadRequest
from .models import User
from .tests import http_response
from django.db import connection
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from .serializers import *

# Create your views here.

class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        register_serializer = UserRegisterSerializer(data=request.data)
        if not register_serializer.is_valid():
            raise ValidationError(
                {
                    'error_message': 'Please correct the following errors.',
                    'errors': register_serializer.errors,
                }
            )
        # saving the details of the registered user
        user = register_serializer.save()
        return http_response(data=self.get_tokens_for_user(user, register_serializer),
                                 message='Register Successfully', status_code=status.HTTP_201_CREATED)

    # generating access token for the user     
    def get_tokens_for_user(self, user, register_serializer):
        refresh = RefreshToken.for_user(user)
        return {
            'user': {'id': user.id,
                     'username': register_serializer.data['username'],
                     'phone': register_serializer.data['phone'], },
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class LoginView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        login_serializer = UserLoginSerializer(data=request.data)
        if not login_serializer.is_valid():
            raise ValidationError(
                {
                    'error_message': 'Please correct the following errors.',
                    'errors': login_serializer.errors,
                }
            )
        founded_user = User.objects.get(phone=request.data['phone'])
        if not founded_user.check_password(login_serializer.data['password']):
            raise BadRequest({'error_message': 'Incorrect authentication credentials.'})
        return http_response(data=self.get_tokens_for_user(founded_user, login_serializer),
                            message='Login Successfully', status_code=status.HTTP_200_OK)

    # generating access token for the user     
    def get_tokens_for_user(self, user, login_serializer):
        refresh = RefreshToken.for_user(user)
        return {
            'user': {'phone': login_serializer.data['phone']},
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class VerifyOtp(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        user_verify_otp_serializer = UserVerifyOtpSerializer(data=request.data)
        if not user_verify_otp_serializer.is_valid():
            raise ValidationError(
                {
                    'error_message': 'Please correct the following errors.',
                    'errors': user_verify_otp_serializer.errors,
                }
            )
        founded_user = User.objects.get(phone=request.data['phone'])
        phone_no = request.data['phone']
        cursor = connection.cursor()
        cursor.execute("update app_user set is_otp_verified = 'true' where phone = '{number}'"
                        .format(number=phone_no))
        return http_response(data=self.get_tokens_for_user(founded_user,user_verify_otp_serializer),
                                    message='Otp verified successfully Successfully',
                                    status_code=status.HTTP_200_OK)
    
    def get_tokens_for_user(self, user, login_serializer):
        refresh = RefreshToken.for_user(user)
        return {
            'user': {'phone': login_serializer.data['phone']},
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class WeatherView(generics.UpdateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = Weather.objects.all()
        serializer = WeatherSerializer(user,many=True)
        return http_response(data=serializer.data, message='Please, update your profile!', 
                            status_code=status.HTTP_200_OK)

class WeatherDataView(generics.UpdateAPIView, generics.RetrieveAPIView, generics.ListAPIView):

    def post(self, request, *args, **kwargs):
        serializer = WeatherSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(
                {
                    'error_message': 'Please correct the following errors.',
                    'errors': serializer.errors,
                }
            )
        serializer.save()
        return http_response(data=serializer.data, message='Please, update your profile!', 
                            status_code=status.HTTP_200_OK)