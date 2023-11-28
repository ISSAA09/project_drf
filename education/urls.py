from django.urls import path

from education.apps import EducationConfig
from rest_framework.routers import DefaultRouter

from education.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonDestroyAPIView, LessonUpdateAPIView, PaymentListAPIView, SubscriberCreateAPIView, \
    SubscriberDeleteAPIView, PaymentCreateAPIView, GetPaymentView

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

                  path('list/', PaymentListAPIView.as_view(), name='payment-list'),

                  path('subscribers/create/', SubscriberCreateAPIView.as_view(), name='subscribers-create'),
                  path('subscribers/delete/<int:pk>/', SubscriberDeleteAPIView.as_view(), name='subscribers-delete'),

                  path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
                  path('payment/<str:payment_id>/', GetPaymentView.as_view(), name='payment_retrieve'),

              ] + router.urls
