from django.urls import path 
from .views import StudentDetailModelReadView, SingleStudentDetailModelReadView

urlpatterns = [
    path("student-details-read/", StudentDetailModelReadView.as_view(), name="StudentDetailModelReadView"),
    path("student-details-read/<id>/", SingleStudentDetailModelReadView.as_view(), name="SingleStudentDetailModelReadView"),
    
]