from django.db import models
from reference.models import Position

import uuid
import os

def get_file_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return os.path.join('teacher/teacher', filename)

# Create your models here.

class Teacher(models.Model):
	class Meta:
		verbose_name = "тренер"
		verbose_name_plural = "тренеры"
	short_name = models.CharField(verbose_name="имя", max_length=40)
	name = models.CharField(verbose_name="полное имя", max_length=255)
	position = models.ForeignKey(Position, verbose_name="должность", on_delete=models.SET_NULL, null=True)
	image = models.FileField(verbose_name="фотография", upload_to=get_file_path)

	def __str__(self):
		return self.name