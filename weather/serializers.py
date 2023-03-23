from rest_framework import serializers
from django.core.mail import send_mail
from django.core.validators import MinLengthValidator
from .models import *

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    password = serializers.CharField(validators=[MinLengthValidator(5)], allow_null=False, required=True,
                                     write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'phone', 'email',  'password']

    def validate_phone(self, attrs):
        user = User.objects.filter(phone=attrs)
        if user.exists():
            raise serializers.ValidationError("This phone number already exist")
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            phone=validated_data['phone'],
            email=validated_data['email'],
        )
        user = User.objects.get(phone=validated_data['phone'])
        user.set_password(validated_data['password'])
        gen_otp = generateotp()
        send_mail('Registration Completed',"Dear user, your OTP for mobile/email id verification with Weather "
                  "application is " + gen_otp + "." +" It is valid for 10 min.", 'example@gmail.com', 
                    [user.email])
        user.save()
        return user
    
def generateotp():
    otp=""
    for i in range(6):
        otp+=str(r.randint(1,9))
    return otp

# User Login serializer using JWT Authentication
class UserLoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['phone','password']

class UserVerifyOtpSerializer(serializers.ModelSerializer):
    otp = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['phone', 'otp']
    
    def validate(self, attrs):
        user = User.objects.get(phone=attrs['phone'])
        if not user.otp == attrs['otp']:
            raise serializers.ValidationError({'otp': "Invalid OTP"})
        return attrs

    def validate_phone(self, attrs):
        user = User.objects.filter(phone=attrs)
        if not user.exists():
            raise serializers.ValidationError("This phone number doesn't exist")
        return attrs
    
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ["country", "city", "temperature", "monday", "tuesday", "wednesday", "thursday", 
            "friday", "saturday", "sunday", "date"]
        
    def create(self, validated_data):
        obj = Weather.objects.create(
            country=self.context['country'],
            city = validated_data['city'],  
            monday = validated_data['monday'],
            tuesday = validated_data['tuesday'],
            wednesday = validated_data['wednesday'],
            thursday = validated_data['thursday'],
            friday = validated_data['friday'],
            saturday = validated_data['saturday'],
            sunday = validated_data['sunday'],
        )
        return obj