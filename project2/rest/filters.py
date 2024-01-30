from django_filters import rest_framework
from .models import Car
class CarFilter(rest_framework.FilterSet):
    # company = rest_framework.CharFilter(lookup_expr='exact')
    # company = rest_framework.CharFilter(lookup_expr='contains')
    # company = rest_framework.CharFilter(lookup_expr='contains')
    id = rest_framework.NumberFilter(lookup_expr='gte')
    # company = rest_framework.CharFilter(lookup_expr='in')

    class Meta:
        model = Car
        fields = ['company','id']