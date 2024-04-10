from django.urls import path
from . import views

urlpatterns = [
    # Oldingi URL-lar
    path('<int:course_id>/join/', views.JoinCourseView.as_view(), name='join-course'),
    path('<int:course_id>/leave/', views.LeaveCourseView.as_view(), name='leave-course'),
    path('<int:course_id>/detail/', views.CourseDetailView.as_view(), name='detail-course'),
]
