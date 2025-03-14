from django.test import TestCase
from .models import WeatherData

class WeatherDataModelTest(TestCase):
    def setUp(self):
        WeatherData.objects.create(
            city="Test City",
            country_code="TC",
            coordinate="0.0, 0.0",
            temperature="25 °C",
            pressure="1013 hPa",
            humidity="50%",
            weather_main="Clear",
            weather_description="Clear sky",
            icon="01d"
        )

    def test_weather_data_str(self):
        weather_data = WeatherData.objects.get(city="Test City")
        self.assertEqual(str(weather_data), "Test City, TC")

class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
