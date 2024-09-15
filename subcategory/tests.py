from django.urls import reverse
from subcategory.models import Subcategory
from category.models import Category
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User


class SubcategoryTestCase(APITestCase):

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

        self.subcategory = Subcategory.objects.create(
            category=self.category,
            name='Test_subcategory',
            slug='Test-subcategory'
        )

    def test_list_subcategory(self):
        response = self.client.get(
            reverse('subcategory:list_subcategory')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            [{'name': 'Test_subcategory', 'image': None}]
        )

    def test_detail_subcategory(self):
        response = self.client.get(
            reverse('subcategory:retrieve_subcategory',
                    args=('Test-subcategory',))
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'name': 'Test_subcategory', 'image': None}
        )
