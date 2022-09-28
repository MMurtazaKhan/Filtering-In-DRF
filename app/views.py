from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters

from .mypagination import Pagination, OffSetPagination

# Create your views here.

class ProductFilter(filters.FilterSet):
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Student
        fields = ['city', 'name']


class StudentAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)

    # filterset_class = ProductFilter

class StudentSearch(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'city']
    # search_fields = ['^name']
    # search_fields = ['=name']


class StudentPagination(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = Pagination
    pagination_class = OffSetPagination