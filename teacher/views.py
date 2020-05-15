from rest_framework.viewsets import ModelViewSet
from .serializers import TeacherSerializer
from .models import Teacher

class TeacherViewSet(ModelViewSet):
	serializer_class = TeacherSerializer
	queryset = Teacher.objects.all()