from django.urls import reverse
from category.models import Category
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User


class CategoryTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.test',
                                        password='test',
                                        is_active=True)
        self.client.force_authenticate(user=self.user)

        self.category = Category.objects.create(
            name='Test_category',
            slug='Test-category'
        )

    def test_list_category(self):
        response = self.client.get(
            reverse('category:list_category')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            [{'name': 'Test_category', 'image': None}]
        )

    def test_detail_category(self):
        response = self.client.get(
            reverse('category:retrieve_category',
                    args=('Test-category',))
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'name': 'Test_category', 'image': None}
        )
