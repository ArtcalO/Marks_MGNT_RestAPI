from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class StudentViewset(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


class CourseViewset(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

class MarkViewset(viewsets.ModelViewSet):
	queryset = Mark.objects.all()
	serializer_class = MarkSerializer

