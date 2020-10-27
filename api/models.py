from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=30)
	subname = models.CharField(max_length=30)
	age = models.IntegerField()

	def __str__(self):
		return f"{self.name} {self.subname}"

class Course(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return f"{self.name}"

class Mark(models.Model):
	student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
	mark = models.IntegerField()

	def __str__(self):
		return f"{self.student} - {self.course} - {self.mark}"
