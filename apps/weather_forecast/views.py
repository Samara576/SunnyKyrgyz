from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from geocoder import ip
import pyowm
from .filters import WeatherFilter
from .serializers import WeatherSerializer

class WeatherViewSet(ViewSet):
    def list(self, request):
        location = request.query_params.get('location')

        if not location:
            g = ip('me')
            location = g.city

        owm = pyowm.OWM('c2cecd6426439815a02f2d2e745409c6')  
        mgr = owm.weather_manager()

        try:
            observation = mgr.weather_at_place(location)
        except pyowm.exceptions.api_response_error.NotFoundError:
            return Response({'error': 'Location not found'}, status=status.HTTP_404_NOT_FOUND)

        w = observation.weather

        data = {
            'location': location,
            'temperature': w.temperature('celsius')['temp'],
            'humidity': w.humidity,
            'weather_description': w.status,
        }

        
        serializer = WeatherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    filter_backends = [DjangoFilterBackend]
    filterset_class = WeatherFilter

