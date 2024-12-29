"""Views for Order Tables / Class
"""

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer


class OrderViewList(APIView):
    """view class for listing all orders in the database"""

    def get(self, request):
        """Handles get request"""

        # pylint: disable=unused-argument
        orders = Order.objects.all() # pylint: disable=no-member

        # serialize extrated data
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Handles a Post request to Orders """

        data = request.data
        deserialized_object = OrderSerializer(data=data)

        if deserialized_object.is_valid():
            deserialized_object.save()
            return Response(deserialized_object.data, status=status.HTTP_201_CREATED)
        return Response(deserialized_object.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(APIView):
    """Gets a Order by id
    Updates an order by Id
    Deletes an order Order by Id
    """

    def get_object(self, pk):
        """Gets an Order object by Id"""

        obj = Order.objects.get(pk=pk) # pylint: disable=no-member
        if obj:
            return obj
        return None

    def get(self, request, pk):
        """Gets an Order by Id"""

        # pylint: disable=unused-argument
        order = self.get_object(pk=pk)

        if order:
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        """Updates an Order instance"""

        order = self.get_object(pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Deletes an order by id"""

        # pylint: disable=unused-argument
        order_to_delete = self.get_object(pk=pk)
        if order_to_delete:
            order_to_delete.delete()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)