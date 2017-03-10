from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from . import models, views

class RoomTests(APITestCase):

    def setUp(self):
        data = {'hostel_name': 'hostel-A'}
        self.hostel = models.Hostel.objects.create(**data)
        self.factory = APIRequestFactory()

    def test_create_hostel(self):
        url = '/quick-start/hostel/'
        data = {'hostel_name': 'hostel-A'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_room(self):
        """
        Ensure we can create a new account object.
        """

        url = '/quick-start/room/'
        view = views.TestView.as_view()
        data = {'hostel': self.hostel.id, 'room_no': '103', 'room_size': '2'}
        request = self.factory.post(url, data=data)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Room.objects.count(), 1)
        self.assertEqual(models.Room.objects.get().room_no, 103)


