from rest_framework.pagination import LimitOffsetPagination


class ReviewPagination(LimitOffsetPagination):
    default_limit = 7
    max_limit = 7
