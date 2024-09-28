from rest_framework import serializers
from .models import Institute, Course, Student, Profile

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(write_only=True)
    student_name = serializers.CharField(source='student.student_name', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'photo', 'resume', 'student_id', 'student_name']

    def create(self, validated_data):
        student_id = validated_data.pop('student_id')
        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            raise serializers.ValidationError({"student_id": "Student does not exist."})

        profile = Profile.objects.create(student=student, **validated_data)
        return profile