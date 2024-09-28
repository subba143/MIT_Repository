from .models import Institute, Course, Student, Profile
from .serializers import InstituteSerializer, CourseSerializer, StudentSerializer, ProfileSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer

    def retrieve(self, request, pk=None):
        try:
            institute = self.get_object()
            serializer = self.get_serializer(institute)
            return Response(serializer.data)
        except Institute.DoesNotExist:
            return Response({'error': 'Institute not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        institute = self.get_object()
        serializer = self.get_serializer(institute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        institute = self.get_object()
        serializer = self.get_serializer(institute, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        institute = self.get_object()
        institute.delete()
        return Response({'message': 'Institute deleted'}, status=status.HTTP_204_NO_CONTENT)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request):
        courses = self.get_queryset()
        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            course = self.get_object()
            serializer = self.get_serializer(course)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        course = self.get_object()
        serializer = self.get_serializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        course = self.get_object()
        serializer = self.get_serializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        course = self.get_object()
        course.delete()
        return Response({'message': 'Course deleted'}, status=status.HTTP_204_NO_CONTENT)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def retrieve(self, request, pk=None):
        try:
            student = self.get_object()
            serializer = self.get_serializer(student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        student = self.get_object()
        serializer = self.get_serializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        student = self.get_object()
        serializer = self.get_serializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student = self.get_object()
        student.delete()
        return Response({'message': 'Student deleted'}, status=status.HTTP_204_NO_CONTENT)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def retrieve(self, request, pk=None):
        try:
            profile = self.get_object()
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        profile = self.get_object()
        profile.delete()
        return Response({'message': 'Profile deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def search(request):
    if request.method == 'GET':
        query = request.query_params.get('q', None)
        if query:
            students = Student.objects.filter(student_name__icontains=query)
            courses = Course.objects.filter(course_name__icontains=query)
            institutes = Institute.objects.filter(institute_name__icontains=query)

            student_serializer = StudentSerializer(students, many=True)
            course_serializer = CourseSerializer(courses, many=True)
            institute_serializer = InstituteSerializer(institutes, many=True)

            return Response({
                'students': student_serializer.data,
                'courses': course_serializer.data,
                'institutes': institute_serializer.data
            }, status=status.HTTP_200_OK)

        return Response({'error': 'No search query provided'}, status=400)

    elif request.method == 'POST':
        student_data = request.data.get('student')
        course_data = request.data.get('course')
        institute_data = request.data.get('institute')

        if student_data:
            student_serializer = StudentSerializer(data=student_data)
            if student_serializer.is_valid():
                student_serializer.save()
                return Response(student_serializer.data, status=status.HTTP_201_CREATED)
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif course_data:
            course_serializer = CourseSerializer(data=course_data)
            if course_serializer.is_valid():
                course_serializer.save()
                return Response(course_serializer.data, status=status.HTTP_201_CREATED)
            return Response(course_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif institute_data:
            institute_serializer = InstituteSerializer(data=institute_data)
            if institute_serializer.is_valid():
                institute_serializer.save()
                return Response(institute_serializer.data, status=status.HTTP_201_CREATED)
            return Response(institute_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Invalid data format'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        student_id = request.data.get('student_id')
        student_data = request.data.get('student')

        if student_id and student_data:
            try:
                student_instance = Student.objects.get(pk=student_id)
                student_serializer = StudentSerializer(student_instance, data=student_data, partial=False)
                if student_serializer.is_valid():
                    student_serializer.save()
                    return Response(student_serializer.data, status=status.HTTP_200_OK)
                return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        student_id = request.data.get('student_id')
        student_data = request.data.get('student')

        if student_id and student_data:
            try:
                student_instance = Student.objects.get(pk=student_id)
                student_serializer = StudentSerializer(student_instance, data=student_data, partial=True)  # partial=True for PATCH
                if student_serializer.is_valid():
                    student_serializer.save()
                    return Response(student_serializer.data, status=status.HTTP_200_OK)
                return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student_id = request.data.get('student_id')

        if student_id:
            try:
                student_instance = Student.objects.get(pk=student_id)
                student_instance.delete()
                return Response({'message': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            except Student.DoesNotExist:
                return Response({'error': 'Std not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Invalid or Error request'}, status=status.HTTP_400_BAD_REQUEST)
