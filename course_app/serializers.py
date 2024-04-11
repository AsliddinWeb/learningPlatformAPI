from rest_framework.serializers import ModelSerializer, SerializerMethodField

from auth_app.serializers import UserSerializer
from .models import Section, Lesson, LessonImage, Category, Course, Author

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class LessonImageSerializer(ModelSerializer):
    class Meta:
        model = LessonImage
        fields = ['title', 'image']

class LessonSerializer(ModelSerializer):
    images = LessonImageSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video', 'description', 'material', 'images']

class SectionSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'title', 'lessons']



class CourseSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    students = UserSerializer(many=True, read_only=True)
    sections = SectionSerializer(many=True, read_only=True)
    is_user_enrolled = SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_user_enrolled(self, obj):
        user = self.context.get('request').user

        return user.is_authenticated and obj.students.filter(pk=user.pk).exists()

class CourseListSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'