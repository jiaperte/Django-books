from django.db import models

# Create your models here.
class Nem(models.Model):
    nmi = models.CharField(max_length=20)
    meter_serial_number = models.CharField(max_length=20)
    reading_value = models.DecimalField(max_digits=10, decimal_places=2)
    reading_date_time = models.DateTimeField()
    flow_file_name = models.CharField(max_length=32)