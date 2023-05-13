from django.core.management import call_command
from django.test import TestCase
from nem_manage.models import Nem
import os
import tempfile

class LoadNEM13DataTest(TestCase):
    def setUp(self):
        # Create a temporary file
        self.test_file = tempfile.NamedTemporaryFile(prefix='test', suffix='.csv', dir='/tmp', delete=False)

        # Write test data to the file
        self.test_file.write(b"100,NEM13,200401101030,MDA1,Ret1,,,,,,,,,,,,,,,,,,\n")
        self.test_file.write(b"250,0123456789ABC,202305021010,S,1,0,123456,,,,,,,123.45,20051023210001,\n")
        self.test_file.close()

    def tearDown(self):
        # Remove the temporary file
        os.unlink(self.test_file.name)

    def test_load_nem13_data(self):
        # Run the management command
        call_command('load_nem13_data', self.test_file.name)

        # Check that a Reading was created
        self.assertEqual(Nem.objects.count(), 1)

        # Get the created Reading
        reading = Nem.objects.first()

        # Check the Reading's fields
        self.assertEqual(reading.nmi, "0123456789ABC")
        self.assertEqual(reading.meter_serial_number, "123456")
        self.assertEqual(float(reading.reading_value), 123.45)
