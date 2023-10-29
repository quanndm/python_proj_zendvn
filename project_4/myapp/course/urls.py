from django.urls import path
from . import views


urlpatterns = [
    path('courses/list/', views.list_course, name='create_course'),
    path('courses/detail/<int:course_id>/', views.detail_course, name='detail_course'),
]
