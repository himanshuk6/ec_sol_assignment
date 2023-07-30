# Import necessary modules for testing
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Place

class PlaceListCreateViewTest(APITestCase):
    def setUp(self):
        # Set up any data that you need for your tests
        self.place_data = {
            "name": "Test Place",
            "description": "This is a test place",
            "latitude": 1.23,
            "longitude": 4.56
        }
        self.url = reverse('place-list')

    def test_create_place(self):
        # Ensure you can create a new Place object using POST request
        response = self.client.post(self.url, self.place_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Place.objects.count(), 1)
        self.assertEqual(Place.objects.get().name, 'Test Place')

    def test_get_place_list(self):
        
        Place.objects.create(**self.place_data)  
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Place')

    def test_search_places(self):
        
        Place.objects.create(**self.place_data)  
        response = self.client.get(self.url, {'q': 'Test Place'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Place')

    def test_search_places_no_results(self):
    
        response = self.client.get(self.url, {'q': 'Nonexistent Place'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  
