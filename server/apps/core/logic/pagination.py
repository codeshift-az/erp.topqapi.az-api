from rest_framework.pagination import PageNumberPagination


class PageLimitPagination(PageNumberPagination):
    """PageLimit pagination class for the API."""

    page_size = 12
    max_page_size = 100
    page_size_query_param = "limit"

    def paginate_queryset(self, queryset, request, view=None):
        """Paginate the queryset if the limit query param is not 'all'."""
        if request.query_params.get("limit") == "all":
            return None

        return super().paginate_queryset(queryset, request, view)
