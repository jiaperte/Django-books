import datetime
from django.test import TestCase
from nem_manage.models import Nem


# Create your tests here.
class NemReadingTestCase(TestCase):
    def setUp(self):
        Nem.objects.create(
            nmi="test_nmi",
            meter_serial_number="0123456789",
            reading_value=10.5,
            reading_date_time="2023-05-12 13:00:00",
            flow_file_name="test_file_name"
        )

    def test_reading_created(self):
        """Reading is correctly created"""
        reading = Nem.objects.get(nmi="test_nmi")
        self.assertEqual(reading.meter_serial_number, '0123456789')
        self.assertEqual(reading.reading_value, 10.5)
        self.assertEqual(reading.reading_date_time.strftime("%Y-%m-%d %H:%M:%S"), '2023-05-12 13:00:00')
        self.assertEqual(reading.flow_file_name, 'test_file_name')
