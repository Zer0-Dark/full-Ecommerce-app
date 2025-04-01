from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import password_validation
from django.contrib.auth import authenticate



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "phone_number", "profile_picture", 'bio')



class RegistrationSerializer(serializers.ModelSerializer):
    # write_only=True: Ensures that passwords are not exposed in API responses aka INPUT ONLY.
    # validators=[password_validation.validate_password]: Applies Django's built-in password strength validation.
    password = serializers.CharField(
        write_only=True, required=True, validators= [password_validation.validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', "phone_number", 'password', 'password2')


    def validate(self, data):
        if data.get("password") != data.get("password2"):
            raise serializers.ValidationError({"password": "Passwords do not match."})
        # Remove password2 from data as it's not needed anymore
        data.pop('password2')
        return data
    
    def create(self, validated_data):
        # Extract the password from validated data
        password = validated_data.pop('password')
        # Create the user instance without the password
        user = CustomUser(**validated_data)
        # Set the hashed password
        user.set_password(password)
        # Save the user to the database
        user.save()
        return user
    
    
class LoginSerializer(serializers.Serializer):
    login_id = serializers.CharField(required=True)  # Single field for email/username/phone
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Extract the login field (email, username, or phone) and password
        login_id = data.get('login_id')
        password = data.get('password')

        if not login_id:
            raise serializers.ValidationError("A login identifier (email, username, or phone) is required.")

        # Authenticate the user based on the provided login field from the custom backend and password
        user = authenticate(request=self.context.get('request'), identifier=login_id, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials. Please check your login details.")

        return user
