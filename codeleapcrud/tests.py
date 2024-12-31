from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Person


class PersonCreateTestCase(APITestCase):
    def test_create_person(self):
        url = reverse("person-create")
        data = {
            "username": "test_user",
            "title": "Test Title",
            "content": "This is a test content",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().username, "test_user")


class PersonListTestCase(APITestCase):
    def setUp(self):
        Person.objects.create(username="user1", title="Title 1", content="Content 1")
        Person.objects.create(username="user2", title="Title 2", content="Content 2")

    def test_list_persons(self):
        url = reverse("person-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class PersonDetailTestCase(APITestCase):
    def setUp(self):
        self.person = Person.objects.create(
            username="user1", title="Title 1", content="Content 1"
        )

    def test_get_person_detail(self):
        url = reverse("person-detail", kwargs={"pk": self.person.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.person.username)


class PersonUpdateTestCase(APITestCase):
    def setUp(self):
        self.person = Person.objects.create(
            username="user1", title="Title 1", content="Content 1"
        )

    def test_update_person(self):
        url = reverse("person-update", kwargs={"pk": self.person.pk})
        data = {"title": "Updated Title", "content": "Updated Content"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.person.refresh_from_db()
        self.assertEqual(self.person.title, "Updated Title")
        self.assertEqual(self.person.content, "Updated Content")


class PersonDeleteTestCase(APITestCase):
    def setUp(self):
        self.person = Person.objects.create(
            username="user1", title="Title 1", content="Content 1"
        )

    def test_delete_person(self):
        url = reverse("person-delete", kwargs={"pk": self.person.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)
