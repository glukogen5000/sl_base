import django_filters
from .models import *


class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = ItemProject
        fields = '__all__'
