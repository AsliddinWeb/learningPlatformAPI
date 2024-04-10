from django.contrib import admin

from .models import *
admin.site.register(Author)
admin.site.register(Category)

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('students', )
admin.site.register(Course, CourseAdmin)

admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(LessonImage)