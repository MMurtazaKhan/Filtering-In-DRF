from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class Pagination(PageNumberPagination):
    page_size = 5

class OffSetPagination(LimitOffsetPagination):
    default_limit = 7
    max_limit = 10
