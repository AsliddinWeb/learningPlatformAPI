from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course

from .serializers import CourseSerializer

class JoinCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        user = request.user
        course = get_object_or_404(Course, pk=course_id)

        if user not in course.students.all():
            course.students.add(user)
            return Response({"message": "You have successfully joined the course."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You are already enrolled in this course."}, status=status.HTTP_400_BAD_REQUEST)

class LeaveCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        user = request.user
        course = get_object_or_404(Course, pk=course_id)

        if user in course.students.all():
            course.students.remove(user)
            return Response({"message": "You have successfully left the course."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You are not enrolled in this course."}, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    """
    Kursning to'liq detallarini qaytaradi, agar foydalanuvchi tizimga kirgan bo'lsa,
    shu jumladan foydalanuvchining kursga qo'shilgan yoki yo'qligini ko'rsatuvchi maydonni ham qaytaradi.
    """
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        # Serializerga so'rov kontekstini o'tkazish
        serializer = CourseSerializer(course, context={'request': request})
        return Response(serializer.data)