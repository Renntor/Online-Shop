from rest_framework.response import Response
from product.models import Product, Cart
from rest_framework import generics
from product.serializers import ProductSerializers, CartSerializers, CartCreateUpdateSerializers
from product.pagination import MyPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    pagination_class = MyPagination


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CartListCreateAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serialize = CartCreateUpdateSerializers(data=request.data)
        if serialize.is_valid():
            cart, created = Cart.objects.get_or_create(
                user=request.user,
                product=serialize.validated_data['product'],
                defaults={'quantity': serialize.validated_data['quantity']}
            )
            if not created:
                cart.quantity += serialize.validated_data['quantity']
                cart.save()
            return Response(Cart(cart).data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
       cart = Cart.objects.filter(user=request.user)
       total = sum([product.price_calculation() for product in cart])
       serializer = Cart(cart, many=True)
       return Response({
           'cart':serializer.data,
           'total_price': total
       })