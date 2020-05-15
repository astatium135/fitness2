from rest_framework.routers import DefaultRouter
from reference.views import PositionViewSet, PlaceViewSet, LessonViewSet
from teacher.views import TeacherViewSet
from group_lesson.views import GroupLessonViewSet

router = DefaultRouter()

router.register('positions', PositionViewSet)
router.register('places', PlaceViewSet)
router.register('lessons', LessonViewSet)

router.register('teacher', TeacherViewSet)

router.register('group_lesson', GroupLessonViewSet)