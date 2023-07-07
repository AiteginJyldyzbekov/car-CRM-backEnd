from django_filters import rest_framework as rest_filters, CharFilter

from cars.models import Car

class CarFilter(rest_filters.FilterSet):
    brand = CharFilter(field_name='brand', lookup_expr='icontains')
    model = CharFilter(field_name='model', lookup_expr='icontains')
    vehicle_type = CharFilter(field_name='vehicle_type', lookup_expr='icontains')
<<<<<<< HEAD
    license_plate = CharFilter(field_name='license_plate', lookup_expr='icontains')
=======
>>>>>>> 32f6fa64928120ba7576a4d4f23db3faf3c59756


    class Meta:
        model = Car
<<<<<<< HEAD
        fields = ['brand','model','vehicle_type', 'license_plate']
=======
        fields = ['brand','model','vehicle_type']
>>>>>>> 32f6fa64928120ba7576a4d4f23db3faf3c59756
