import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class EventSearchFilter(django_filters.FilterSet):
    eventdate = DateFilter(field_name='event_date', lookup_expr='gte')
    eventname = CharFilter(field_name='event_name', lookup_expr='icontains')
    class Meta:
        model = Event
        fields = ['event_name', 'event_date']
        widgets = [

        ]
