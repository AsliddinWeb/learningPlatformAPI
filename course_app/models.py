from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=455)
    image = models.ImageField(upload_to='authors/')
    description = models.TextField()
    email = models.CharField(max_length=455)
    phone = models.CharField(max_length=455)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=455)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.title

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=455)
    banner_image = models.ImageField(upload_to='banner-images/')
    intro_video = models.TextField()
    course_time = models.CharField(max_length=455)
    description = models.TextField()
    students_count = models.CharField(max_length=455)
    students = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=455)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    # Course maydonini olib tashlaymiz, chunki biz Section orqali kursga murojaat qilamiz
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=455)
    video = models.TextField(null=True, blank=True)
    description = models.TextField()
    material = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return self.title

class LessonImage(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=455)
    image = models.ImageField(upload_to='lesson-images/')

    def __str__(self):
        return self.title
