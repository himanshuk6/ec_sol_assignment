# your_project_name/urls.py
from django.urls import path
from .views import PlaceListCreateView, PlaceCreateAPIView, PlaceDeleteAPIView, PlaceSearchAPIView, place_list_view, api_details
urlpatterns = [
    path('places/', PlaceListCreateView.as_view(), name='place-list'),
    path('places/create/', PlaceCreateAPIView.as_view(), name='place-create'),
    path('places/<int:pk>/delete/', PlaceDeleteAPIView.as_view(),name='place-delete'),
    path('places/search/', PlaceSearchAPIView.as_view(),name='place-search'),
    path('places/list/', place_list_view, name='place-list-html'),
    path('', api_details, name='api-details-html'),
]
