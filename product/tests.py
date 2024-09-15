from django.urls import reverse
from subcategory.models import Subcategory
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from product.models import Product, Cart
from category.models import Category


class ProductTestCase(APITestCase):

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

        self.product = Product.objects.create(
            subcategory=self.subcategory,
            name='Test_product',
            slug='Test-product',
            price=199
        )

    def test_list_product(self):
        response = self.client.get(
            reverse('product:list_product')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'name': 'Test_product', 'price': 199,
              'subcategory': {'name': 'Test_subcategory', 'category': {'name': 'Test_category'}}, 'image': []}]

        )
