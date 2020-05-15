from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import GroupLesson
from teacher.serializers import TeacherSerializer
from reference.serializers import PlaceSerializer, LessonSerializer

class GroupLessonSerializer(ModelSerializer):
	place = serializers.ReadOnlyField(source="place.name", read_only=True)
	name = serializers.ReadOnlyField(source="lesson.name", read_only=True)
	description = serializers.ReadOnlyField(source="lesson.description", read_only=True)
	teacher = TeacherSerializer()
	class Meta:
		model = GroupLesson
		#fields = ('__all__')
		exclude = ('lesson', )