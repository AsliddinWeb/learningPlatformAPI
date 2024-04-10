from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/join/', views.JoinCourseView.as_view(), name='join-course'),
    path('<int:course_id>/leave/', views.LeaveCourseView.as_view(), name='leave-course'),
    path('<int:course_id>/detail/', views.CourseDetailView.as_view(), name='detail-course'),

    path('all/', views.CourseListView.as_view(), name='course-list'),
    
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
]
