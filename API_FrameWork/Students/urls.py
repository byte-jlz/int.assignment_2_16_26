from django.urls import path
from .views import StudentList, StudentDetail

urlpatterns = [
    path('profiles/', StudentList.as_view(), name='student-list'),
    path('profiles/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
    path('profiles/<int:pk>/update/', StudentDetail.as_view(), name='student-update'),
    path('profiles/<int:pk>/delete/', StudentDetail.as_view(), name='student-delete'),
]