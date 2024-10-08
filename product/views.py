from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_404_NOT_FOUND

from product.models import Product, Cart
from rest_framework import generics
from product.serializers import ProductSerializers, CartCreateUpdateSerializers, CartDestroy, CartsDestroy
from product.pagination import MyPagination
from rest_framework.permissions import IsAuthenticated


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    pagination_class = MyPagination
    lookup_field = 'slug'


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CartListCreateAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartCreateUpdateSerializers

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']

        cart, created = Cart.objects.get_or_create(
            user=self.request.user,
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart.quantity += quantity
            cart.save()
        if quantity == 0:
            cart.delete()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        total = sum([product.price_calculation() for product in queryset])

        return Response({
            'cart': serializer.data,
            'total_price': total
        })


class CartUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartCreateUpdateSerializers

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        data = request.data
        serialize = self.get_serializer(data=data)
        serialize.is_valid(raise_exception=True)
        try:
            cart = Cart.objects.get(
                user=self.request.user,
                product=data['product']
            )
            if data['quantity'] == 0:
                cart.delete()
                return Response(
                    {}
                )
            cart.quantity = data['quantity']
            cart.save()
            return Response(
                self.get_serializer(cart).data
            )
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CartDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartDestroy

    def destroy(self, request, *args, **kwargs):
        data = request.data
        cart = Cart.objects.get(
            user=self.request.user,
            product=data['product']
        )
        cart.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class CartsDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartsDestroy

    def destroy(self, request, *args, **kwargs):
        carts = Cart.objects.filter(user=self.request.user)
        [cart.delete() for cart in carts]
        return Response(status=status.HTTP_202_ACCEPTED)
