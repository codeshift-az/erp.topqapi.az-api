from django.db import models
from django_filters import rest_framework as filters

from server.apps.staff.models import Driver, Seller, Worker


class DriverFilter(filters.FilterSet):
    """FilterSet class for Driver model."""

    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Driver
        fields = (
            "id",
            "name",
        )


class SellerFilter(filters.FilterSet):
    """FilterSet class for Seller model."""

    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    branch = filters.CharFilter(field_name="branch__name", lookup_expr="icontains")
    branch_id = filters.NumberFilter(field_name="branch")

    class Meta:
        model = Seller
        fields = (
            "id",
            "name",
            "branch",
            "branch_id",
        )


class WorkerFilter(filters.FilterSet):
    """FilterSet class for Worker model."""

    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    date = filters.DateFilter(method="filter_by_date")

    order_id = filters.NumberFilter(method="filter_by_order_id")

    class Meta:
        model = Worker
        fields = (
            "id",
            "name",
        )

    def filter_by_date(self, queryset, name, value):
        """Filter queryset by which does not have any order that day"""

        order_id = self.request.query_params.get("order_id")

        if order_id:
            return queryset.exclude(models.Q(orders__install_date=value) & ~models.Q(orders__id=order_id))

        return queryset.exclude(orders__install_date=value)

    def filter_by_order_id(self, queryset, name, value):
        """Filter queryset by order_id"""
        return queryset
