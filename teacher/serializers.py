from rest_framework.serializers import ModelSerializer
from .models import Teacher
from rest_framework import serializers
from reference.serializers import PositionSerializer

class TeacherSerializer(ModelSerializer):
	#position = PositionSerializer()
	position = serializers.ReadOnlyField(source='position.name', read_only=True)

	class Meta:
		model = Teacher
		fields = ('__all__')