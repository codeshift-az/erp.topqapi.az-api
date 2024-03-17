from django_filters import rest_framework as filters

from server.apps.staff.models import Driver, Seller, Worker


class DriverFilter(filters.FilterSet):
    """FilterSet class for Driver model."""

    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Driver
        fields = ("name",)


class SellerFilter(filters.FilterSet):
    """FilterSet class for Seller model."""

    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    branch = filters.CharFilter(field_name="branch__name", lookup_expr="icontains")
    branch_id = filters.NumberFilter(field_name="branch")

    class Meta:
        model = Seller
        fields = (
            "name",
            "branch",
            "branch_id",
        )


class WorkerFilter(filters.FilterSet):
    """FilterSet class for Worker model."""

    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Worker
        fields = ("name",)
