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
        fields = ['id', 'title', 'video', 'description', 'material', 'images', 'duration']

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
        print("User:", user)

        # Check if the user is authenticated
        if not user.is_authenticated:
            return False

        student_pks = obj.students.values_list('pk', flat=True)

        is_enrolled = user.pk in student_pks

        print("Is enrolled:", is_enrolled)
        return is_enrolled


class CourseListSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

class LessonDetailSerializer(ModelSerializer):
    images = LessonImageSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = "__all__"