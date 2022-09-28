
from struct import pack
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.StudentAPI.as_view()),
    path('student-search/', views.StudentSearch.as_view()),
    path('student-pagination/', views.StudentPagination.as_view()),
]
