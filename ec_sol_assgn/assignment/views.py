from rest_framework import generics
from django.contrib.postgres.search import SearchVector
from .models import Place
from .serializers import PlaceSerializer
from django.shortcuts import render


class PlaceListCreateView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceCreateAPIView(generics.CreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceDeleteAPIView(generics.DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceSearchAPIView(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('q', '')
        if search_query:
            return Place.objects.annotate(search=SearchVector('name', 'description')).filter(search=search_query)
        else:
            return Place.objects.none()

def place_list_view(request):
    return render(request, 'places_list.html')

def api_details(request):
    return render(request, 'index.html')
