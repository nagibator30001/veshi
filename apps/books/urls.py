from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.books.views import BookAPI

router = DefaultRouter()
router.register('api_books', BookAPI, basename='books')

urlpatterns = [

]

urlpatterns += router.urls


