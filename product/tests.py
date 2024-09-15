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

    def test_detail_product(self):
        response = self.client.get(
            reverse('product:retrieve_product',
                    args=('Test-product',))
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'name': 'Test_product', 'price': 199,
             'subcategory': {'name': 'Test_subcategory', 'category': {'name': 'Test_category'}}, 'image': []}

        )


class CartTestCase(APITestCase):

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
        self.cart = Cart.objects.create(
            user=self.user,
            product=self.product,
            quantity=10
        )

    def test_detail_cart(self):
        response = self.client.get(
            reverse('product:list_create_cart')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'cart': [{'product': 4, 'product_name': 'Test_product', 'quantity': 10}], 'total_price': 1990}
        )

    def test_create_cart(self):
        response = self.client.post(
            reverse('product:list_create_cart'),
            data={
                "product": self.product.id,
                "quantity": 2
            })

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'product': 1, 'product_name': 'Test_product', 'quantity': 2}
        )

    def test_update_cart(self):
        response = self.client.patch(
            reverse('product:update_cart'),
            data={
                'product': self.product.id,
                "quantity": 5
            })
        self.assertEqual(
            response.json(),
            {'product': self.product.id, 'product_name': 'Test_product', 'quantity': 5}
        )

    def test_destroy_cart(self):
        response = self.client.delete(
            reverse('product:destroy_cart'),
            data={'product': self.product.id}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_202_ACCEPTED
        )

    def test_destroy_carts(self):
        response = self.client.delete(
            reverse('product:destroy_carts')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_202_ACCEPTED
        )
