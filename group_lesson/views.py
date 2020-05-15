from rest_framework.viewsets import ModelViewSet
from .serializers import GroupLessonSerializer
from .models import GroupLesson

class GroupLessonViewSet(ModelViewSet):
	serializer_class = GroupLessonSerializer
	queryset = GroupLesson.objects.all()
