from .models import Course, Author, Category

from auth_app.serializers import UserSerializer


from rest_framework import serializers
from .models import Section, Lesson, LessonImage

class LessonImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonImage
        fields = ['title', 'image']

class LessonSerializer(serializers.ModelSerializer):
    images = LessonImageSerializer(many=True, read_only=True)  # LessonImage'lar uchun

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video', 'description', 'material', 'images']

class SectionSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'title', 'lessons']



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    students = UserSerializer(many=True, read_only=True)
    sections = SectionSerializer(many=True, read_only=True)  # Kursga tegishli bo'limlar
    is_user_enrolled = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_user_enrolled(self, obj):
        user = self.context.get('request').user

        return user.is_authenticated and obj.students.filter(pk=user.pk).exists()