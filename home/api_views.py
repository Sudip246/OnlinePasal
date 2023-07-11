from django.http import Http404
from rest_framework import viewsets, generics, filters, status
from rest_framework.response import Response

from .models import *
from .serializers import *
import django_filters.rest_framework


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'brand', 'status', 'labels']
    search_fields = ['name', 'description', 'labels']
    ordering_fields = ['id', 'price', 'discounted_price']


from rest_framework.views import APIView


class ProductDetailView(APIView):
    """
        Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = ProductSerializer(date = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST )

    def put(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'image', 'slug']
    search_fields = ['name', "slug"]
    ordering_fields = ['slug']


class CategoryDetailView(APIView):
    """
        Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = CategorySerializer(date = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST )

    def put(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'image', 'slug']
    search_fields = ['name', "slug"]
    ordering_fields = ['slug']


class BrandDetailView(APIView):
    """
        Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = BrandSerializer(snippet)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = BrandSerializer(date = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST )

    def put(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = BrandSerializer(snippet, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdListView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'image', "description", 'ranks']
    search_fields = ['name', 'description', "rank"]
    ordering_fields = ['name', "rank"]


class AdDetailView(APIView):
    """
        Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Ad.objects.get(pk=pk)
        except Ad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = AdSerializer(snippet)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = AdSerializer(date = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST )

    def put(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = AdSerializer(snippet, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class SliderListView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'image', "description", 'url']
    search_fields = ['name', 'description', "url"]
    ordering_fields = ['name', "url"]


class SliderDetailView(APIView):
    """
        Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Slider.objects.get(pk=pk)
        except Slider.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = SliderSerializer(snippet)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = SliderSerializer(date = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST )

    def put(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = SliderSerializer(snippet, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)