from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileListAPIView, UserProfileDetailAPIView, PropertyListAPIView,
                    PropertyDetailAPIView, PropertyImagesView,
                    BookingView, ReviewListAPIView, ReviewDetailAPIView, ReviewCreateAPIView,
                    FavoriteView, FavoriteItemView, CityView, RegisterView, LogoutView, CustomLoginView)

router = routers.SimpleRouter()

router.register(r'city', CityView, basename='city_list')
router.register(r'property_image', PropertyImagesView, basename='property_image_list')
router.register(r'booking', BookingView, basename='booking_list')
router.register(r'favorite', FavoriteView, basename='favorite_list')
router.register(r'favorite_item', FavoriteItemView, basename='favorite_item_list')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('auth/users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('property/', PropertyListAPIView.as_view(), name='property_list'),
    path('property/<int:pk>/', PropertyDetailAPIView.as_view(), name='property_detail'),
    path('reviews/', ReviewListAPIView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review_detail'),
    path('reviews/create/<int:pk>/', ReviewCreateAPIView.as_view(), name='review_create'),
]
