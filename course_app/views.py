from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.filters import SearchFilter

from django.shortcuts import get_object_or_404

from .models import Course, Author, Category
from .serializers import CourseSerializer, CourseListSerializer, AuthorSerializer, CategorySerializer


class CourseListView(ListAPIView):
    serializer_class = CourseListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', 'author__name']

class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

class JoinCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        user = request.user
        course = get_object_or_404(Course, pk=course_id)

        if user not in course.students.all():
            course.students.add(user)
            return Response({"message": "Tabriklaymiz. Kursga muvaffaqqiyatli obuna bo'ldingiz!"}, status=HTTP_200_OK)
        else:
            return Response({"message": "Siz allaqachon kursni sotib olgansiz!"}, status=HTTP_400_BAD_REQUEST)

class LeaveCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        user = request.user
        course = get_object_or_404(Course, pk=course_id)

        if user in course.students.all():
            course.students.remove(user)
            return Response({"message": "Tabriklaymiz. Kursga obunani bekor qildingiz!"}, status=HTTP_200_OK)
        else:
            return Response({"message": "Siz xali kursga obuna bo'lmagansiz!"}, status=HTTP_400_BAD_REQUEST)


class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class AuthorDetailView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'