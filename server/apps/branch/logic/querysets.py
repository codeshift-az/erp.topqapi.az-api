from django.db import models


class BranchQuerySet(models.QuerySet):
    """QuerySet definition for Branch model."""

    def get_related(self):
        """Select/Prefetch all relations."""
        return self.select_related(
            "user",
        ).prefetch_related(
            "orders",
        )
