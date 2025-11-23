import django_filters
from .models import Property, City

class PropertyFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='lte')

    guests_min = django_filters.NumberFilter(field_name='max_guests', lookup_expr='gte')
    guests_max = django_filters.NumberFilter(field_name='max_guests', lookup_expr='lte')

    city = django_filters.ModelChoiceFilter(
        queryset=City.objects.all(),
        field_name='city',
    )

    property_type = django_filters.ChoiceFilter(
        choices=Property.PROPERTY_CHOICES
    )

    rules = django_filters.ChoiceFilter(
        choices=Property.RULES_CHOICES
    )

    is_active = django_filters.BooleanFilter()

    class Meta:
        model = Property
        fields = [
            'price_min', 'price_max',
            'guests_min', 'guests_max',
            'city',
            'property_type',
            'rules',
            'is_active'
        ]
