from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Nem

@admin.register(Nem)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ('nmi', 'meter_serial_number', 'reading_value', 'reading_date_time', 'flow_file_name')
    search_fields = ('nmi', 'meter_serial_number',)