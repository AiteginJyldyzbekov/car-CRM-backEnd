from django_filters import rest_framework as rest_filters, CharFilter

from users.models import User

class UserFilter(rest_filters.FilterSet):
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains')
    rented_date = CharFilter(field_name='rented_date', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['first_name','last_name','rented_date']
