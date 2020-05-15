from rest_framework.viewsets import ModelViewSet
from .serializers import PositionSerializer, PlaceSerializer, LessonSerializer
from .models import Position, Place, Lesson

class PositionViewSet(ModelViewSet):
	serializer_class = PositionSerializer
	queryset = Position.objects.all()

class PlaceViewSet(ModelViewSet):
	serializer_class = PlaceSerializer
	queryset = Place.objects.all()

class LessonViewSet(ModelViewSet):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.all()
