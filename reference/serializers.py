from rest_framework.serializers import ModelSerializer
from .models import Position, Place, Lesson

class PositionSerializer(ModelSerializer):
	class Meta:
		model = Position
		fields = ('id', 'name')

class PlaceSerializer(ModelSerializer):
	class Meta:
		model = Place
		fields = ('id', 'name')

class LessonSerializer(ModelSerializer):
	class Meta:
		model = Lesson
		fields = ('id', 'name', 'description')