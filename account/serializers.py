from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ["username", "password"]
        
class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            'password': {"write_only": True}
        }
        
    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            detail = {
                "detail":"User already exist!"
            }
            raise ValidationError(detail=detail)
        return username
    
    def validate(self, instance):
        if instance['password'] != instance['password2']:
            raise ValidationError({"message": "Both password must match"})
        
        if User.objects.filter(email=instance['email']).exists():
            raise ValidationError({"message":"Email already taken"})
        
        return instance
    
    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user