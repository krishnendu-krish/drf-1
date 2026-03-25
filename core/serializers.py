from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name is required")
        return value
    def validate_email(seld, value):
        if Student.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
        