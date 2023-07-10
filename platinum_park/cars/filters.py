from django_filters import rest_framework as rest_filters, CharFilter

from cars.models import Car

class CarFilter(rest_filters.FilterSet):
    brand = CharFilter(field_name='brand', lookup_expr='icontains')
    model = CharFilter(field_name='model', lookup_expr='icontains')
    vehicle_type = CharFilter(field_name='vehicle_type', lookup_expr='icontains')
    license_plate = CharFilter(field_name='license_plate', lookup_expr='icontains')


    class Meta:
        model = Car
        fields = ['brand','model','vehicle_type', 'license_plate']
