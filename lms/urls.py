from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonCreateAPIView, LessonDeleteAPIView, LessonListAPIView, LessonUpdateAPIView, \
    LessonRetrieveAPIView, PaymentListAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lesson/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson-delete'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),

                  path('payments/', PaymentListAPIView.as_view(), name='payments'),

                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
              ] + router.urls
