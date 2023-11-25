from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from education.models import Course, Lesson, Payment, Subscriber
from education.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='video_link')]


class LessonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', read_only=True, many=True)
    subscription_status = serializers.SerializerMethodField(read_only=True)

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.id).count()

    def get_subscription_status(self, obj):
        try:
            subscription = Subscriber.objects.get(
                course_id=obj.pk,
                user_id=self.context['request'].user.pk)

        except ObjectDoesNotExist:
            return False

        else:
            return subscription.is_active_subscription

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
