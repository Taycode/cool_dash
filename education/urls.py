from django.urls import path
from .views import SearchCourseView, CourseView

urlpatterns = [
    path('course/search/', SearchCourseView.as_view()),
    path('course/<str:code>/', CourseView.as_view())
]
