from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets

# Category
from server.apps.category.logic.filters import CategoryFilter
from server.apps.category.logic.serializers import CategorySerializer
from server.apps.category.models import Category

# Core
from server.apps.core.logic.responses import BAD_REQUEST, FORBIDDEN, NOT_FOUND, UNAUTHORIZED


class CategoryViewSet(viewsets.ModelViewSet):
    """Viewset for Category model."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filterset_class = CategoryFilter
    search_fields = ["name"]
    ordering_fields = ["name", "updated_at", "created_at"]

    @extend_schema(
        responses={
            status.HTTP_200_OK: CategorySerializer,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
        },
    )
    def list(self, request, *args, **kwargs):
        """Retrieve list of all categories."""

        return super().list(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_200_OK: CategorySerializer,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
            status.HTTP_404_NOT_FOUND: NOT_FOUND,
        },
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrieve a category by id."""

        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_201_CREATED: CategorySerializer,
            status.HTTP_400_BAD_REQUEST: BAD_REQUEST,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
        },
    )
    def create(self, request, *args, **kwargs):
        """Create a new category."""

        return super().create(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_200_OK: CategorySerializer,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
            status.HTTP_404_NOT_FOUND: NOT_FOUND,
        },
    )
    def update(self, request, *args, **kwargs):
        """Update an existing category by id."""

        return super().update(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
        },
    )
    def destroy(self, request, *args, **kwargs):
        """Delete an existing category by id."""

        return super().destroy(request, *args, **kwargs)
