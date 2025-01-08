from django_filters import FilterSet
from .models import *


class DoctorFilter(FilterSet):
    class Meta:
        model = Doctor
        fields = {
            'department': ['exact'],
            'speciality': ['exact'],
            'price': ['gt', 'lt'],
            'working_days': ['exact'],
        }
