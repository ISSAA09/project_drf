from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Lesson, Course, Subscriber
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='iska29@inbox.ru',
            password='test',
            is_active=True,
            is_staff=True,
            is_superuser=True,
            role="moderator"
        )
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(title="Python Developer")

        self.lesson = Lesson.objects.create(
            title='test',
            description='Test',
            owner=self.user,
            video_link='https://www.youtube.com/watch?v=...'
        )

    def test_create_lesson(self):
        data = {
            'title': self.lesson.title,
            'description': self.lesson.description,
            'course': self.course.id,
            'video_link': self.lesson.video_link
        }

        response = self.client.post(
            reverse('education:lesson_create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(response.json(), {
            'id': 2,
            'title': 'test',
            'description': 'Test',
            'photo': None,
            'video_link': 'https://www.youtube.com/watch?v=...',
            'course': 1,
            'owner': 1
        })

    def test_list_lesson(self):
        response = self.client.get(
            reverse("education:lesson_list")
        )
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(), {'count': 1,
                                            'next': None,
                                            'previous': None,
                                            'results': [
                                                {'id': self.lesson.pk,
                                                 'title': 'test',
                                                 'description': 'Test',
                                                 'photo': None,
                                                 'video_link': 'https://www.youtube.com/watch?v=...',
                                                 'course': None,
                                                 'owner': self.lesson.owner_id}]})

    def test_destroy_lesson(self):
        response = self.client.delete(
            reverse("education:lesson_delete",
                    args=[self.lesson.pk])
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_lesson(self):
        response = self.client.patch(
            reverse("education:lesson_update",
                    args=[self.lesson.pk]),
            data={"title": "Lesson 2 test"}
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.json(), {
            "id": self.lesson.pk,
            "title": "Lesson 2 test",
            "description": self.lesson.description,
            "owner": self.lesson.owner_id,
            "photo": None,
            "video_link": self.lesson.video_link,
            "course": None,
        })

    def test_detail_lesson(self):
        response = self.client.get(
            reverse("education:lesson_get",
                    args=[self.lesson.pk])
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.json(), {
            "id": self.lesson.pk,
            "title": self.lesson.title,
            "description": self.lesson.description,
            "owner": self.lesson.owner_id,
            "photo": None,
            "video_link": self.lesson.video_link,
            "course": None,
        })

    def tearDown(self):
        User.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()


class SubscriberTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='iska29@inbox.ru',
            password='Q1234567',
            is_active=True,
            is_staff=True,
            is_superuser=True,
            role="moderator"
        )
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title="Python Developer",
            description='2.2'
        )

    def test_create_subscriber(self):
        data = {
            'course': self.course.pk
        }
        response = self.client.post(
            reverse('education:subscribers-create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_destroy_subscriber(self):
        sub_create = Subscriber.objects.create(
            course=self.course
        )

        response = self.client.delete(
            reverse("education:subscribers-delete",
                    args=[sub_create.pk])
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
