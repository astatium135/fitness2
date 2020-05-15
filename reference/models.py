from django.db import models

# Create your models here.
class ReferenceModel(models.Model):
	class Meta:
		abstract = True
	name = models.CharField(verbose_name="Имя", max_length=40)
	def __str__(self):
		return self.name
class Position(ReferenceModel):
	class Meta:
		verbose_name = "должность"
		verbose_name_plural = "должности"
class Place(ReferenceModel):
	class Meta:
		verbose_name = "место занятия"
		verbose_name_plural = "места занятий"
class Lesson(ReferenceModel):
	class Meta:
		verbose_name = "вид тренировки"
		verbose_name_plural = "виды тренировок"
	description = models.TextField(verbose_name="описание")