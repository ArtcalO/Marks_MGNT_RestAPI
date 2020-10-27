from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('students', StudentViewset)
router.register('courses', CourseViewset)
router.register('marks', MarkViewset)

urlpatterns = [
    path('', include(router.urls)),
]