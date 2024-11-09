from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
# Create your views here.
from apps.books.models import Book
from apps.books.serializers import BookSerializer

class Pagination(PageNumberPagination):
	page_size = 10
	max_page_size = 10

class BookAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
			  mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	pagination_class = Pagination
