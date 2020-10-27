from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = "__all__"

class MarkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mark
		fields = "__all__"
		# depth = 1

	def create(self, validated_data):
		obj = Mark(
			student = validated_data['student'],
			course=validated_data['course'],
			mark=validated_data['mark'])
		obj.save()
		return obj
		