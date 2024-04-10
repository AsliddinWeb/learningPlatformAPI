from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from .models import Course, Author

from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import CourseSerializer, CourseListSerializer, AuthorSerializer

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
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        serializer = CourseSerializer(course, context={'request': request})
        return Response(serializer.data)

class CourseListView(ListAPIView):
    serializer_class = CourseListSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'author__name']

    def get_queryset(self):
        queryset = Course.objects.all()

        return queryset

class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class AuthorDetailView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'