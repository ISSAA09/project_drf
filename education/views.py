from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from education.models import Course, Lesson, Payment, Subscriber
from education.paginators import CoursesPaginator
from education.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriberSerializer, \
    LessonUpdateSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from education.services import create_payment, retrieve_payment
from education.tasks import send_mail_notification
from users.models import UserRole
from users.permissions import IsOwner, IsModerator, IsSubscriber, IsMember


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursesPaginator

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsModerator]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsModerator | IsOwner | IsSubscriber]
        elif self.action == 'update' or self.action == 'destroy' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def perform_update(self, serializer):
        updated_course = serializer.save()

        course_name = Course.objects.get(pk=updated_course.pk).title
        sub = Subscriber.objects.values("email").filter(course_id=updated_course.pk)
        for email in sub:
            send_mail_notification.delay(email['email'], course_name)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = CoursesPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonUpdateSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_type')
    ordering_fields = ('date_payment',)


class GetPaymentView(APIView):

    def get(self, request, payment_id):
        payment_retrieve = retrieve_payment(payment_id)
        return Response({
            'payment_retrieve': payment_retrieve,
            'status': payment_retrieve.status,
        })


class PaymentCreateAPIView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        pay = create_payment(payment.payment_amount)
        payment.stripe_payment_id = pay['id']
        pay.save()
        payment.save()
        return super().perform_create(serializer)


class SubscriberCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriberSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_subscription = serializer.save()
        new_subscription.user = self.request.user
        new_subscription.email = self.request.user.email
        new_subscription.save()


class SubscriberDeleteAPIView(generics.DestroyAPIView):
    queryset = Subscriber.objects.all()
    permission_classes = [IsAuthenticated]
