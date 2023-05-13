import csv
from datetime import datetime
from django.core.management.base import BaseCommand

from nem_manage.models import Nem


class Command(BaseCommand):
    help = 'Load NEM13 data into the database'

    def add_arguments(self, parser):
        parser.add_argument('nem13_files', nargs='+', type=str)

    def handle(self, *args, **options):
        for nem13_file in options['nem13_files']:
            with open(nem13_file, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] == '250':  # meter data record row
                        nmi = row[1]
                        meter_serial_number = row[6]
                        reading_value = row[13]
                        reading_date_time = row[14]
                        flow_file_name = nem13_file
                        Nem.objects.create(
                            nmi=nmi,
                            meter_serial_number=meter_serial_number,
                            reading_value=reading_value,
                            reading_date_time=datetime.strptime(reading_date_time, "%Y%m%d%H%M%S"),
                            flow_file_name=flow_file_name
                        )
