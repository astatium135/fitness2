from django.db import models

from reference.models import Place, Lesson
from teacher.models import Teacher

class GroupLesson(models.Model):
	class Meta:
		verbose_name = "групповая тренировка"
		verbose_name_plural = "групповые тренировки"
	lesson = models.ForeignKey(Lesson, verbose_name="вид тренировки", on_delete=models.CASCADE)
	place = models.ForeignKey(Place, verbose_name="место проведения", on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher, verbose_name="тренер", on_delete=models.CASCADE)
	startTime = models.TimeField(verbose_name="Время начала занятий")
	endTime = models.TimeField(verbose_name="Время окончания занятий")
	weekDay = models.IntegerField(verbose_name="день недели", choices=((1, "понедельник"),
		(2, "вторник"),
		(3, "среда"),
		(4, "четверг"),
		(5, "пятница"),
		(6, "субота"),
		(7, "воскресенье")))
	pay = models.DecimalField(max_digits=6, verbose_name="Плата", decimal_places=2, blank=True, default=0)
	availability = models.PositiveIntegerField(verbose_name="Свободно мест", default=0)

	def __str__(self):
		return "%s %s %s - %s" % (self.lesson.name, self.place.name, self.startTime, self.endTime)