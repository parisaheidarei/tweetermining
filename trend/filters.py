import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class HashtagTrendFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="createDate", lookup_expr='gte')
    end_date = DateFilter(field_name="createDate", lookup_expr='lte')
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = HashtagTrend
        fields = '__all__'
        exclude = ['preRepeat','repeat', 'createDate']

   
