from django.urls import path
from . import views

urlpatterns = [
    # Courses
    path('<int:course_id>/join/', views.JoinCourseView.as_view(), name='join-course'),
    path('<int:course_id>/leave/', views.LeaveCourseView.as_view(), name='leave-course'),
    path('<int:pk>/detail/', views.CourseDetailView.as_view(), name='detail-course'),
    path('all/', views.CourseListView.as_view(), name='course-list'),

    # Authors
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),

    # Cateogiries
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
]
