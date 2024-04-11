from django.contrib import admin

from .models import *

# Inlines
class SectionInline(admin.TabularInline):
    model = Section
    fields = ["title"]

class LessonInline(admin.TabularInline):
    model = Lesson
    fields = ["title", "video", "description", "material"]

class LessonImageInline(admin.TabularInline):
    model = LessonImage
    fields = ["title", "image"]

# Admin registers
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'banner_image', 'intro_video', 'course_time', 'students_count']
    filter_horizontal = ('students', )
    list_filter = ['category', 'author']
    inlines = [SectionInline]
admin.site.register(Course, CourseAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'email', 'phone']
admin.site.register(Author, AuthorAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']
admin.site.register(Category, CategoryAdmin)

class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    inlines = [LessonInline]
admin.site.register(Section, SectionAdmin)

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'video', 'description', 'material', 'section']
    inlines = [LessonImageInline]
admin.site.register(Lesson, LessonAdmin)

class LessonImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'lesson']
admin.site.register(LessonImage, LessonImageAdmin)