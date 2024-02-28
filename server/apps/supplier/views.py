from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets

# Core
from server.apps.core.logic.responses import BAD_REQUEST, FORBIDDEN, NOT_FOUND, UNAUTHORIZED

# Supplier
from server.apps.supplier.logic.filters import SupplierFilter
from server.apps.supplier.logic.serializers import SupplierSerializer
from server.apps.supplier.models import Supplier


class SupplierViewSet(viewsets.ModelViewSet):
    """Viewset for Supplier model."""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    filterset_class = SupplierFilter
    search_fields = ("name",)
    ordering_fields = (
        "name",
        "updated_at",
        "created_at",
    )

    @extend_schema(
        responses={
            status.HTTP_200_OK: SupplierSerializer,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
        },
    )
    def list(self, request, *args, **kwargs):
        """Retrieve list of all suppliers."""

        return super().list(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_200_OK: SupplierSerializer,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
            status.HTTP_404_NOT_FOUND: NOT_FOUND,
        },
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrieve a supplier by id."""

        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_201_CREATED: SupplierSerializer,
            status.HTTP_400_BAD_REQUEST: BAD_REQUEST,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
        },
    )
    def create(self, request, *args, **kwargs):
        """Create a new supplier."""

        return super().create(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_200_OK: SupplierSerializer,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
            status.HTTP_404_NOT_FOUND: NOT_FOUND,
        },
    )
    def update(self, request, *args, **kwargs):
        """Update an existing supplier by id."""

        return super().update(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
        },
    )
    def destroy(self, request, *args, **kwargs):
        """Delete an existing supplier by id."""

        return super().destroy(request, *args, **kwargs)
