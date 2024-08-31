from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created_at`` and ``updated_at`` fields.
    """

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class SlugModel(TimeStampedModel):
    """
    An abstract base class model that provides a ``slug`` field.
    The timestamp fields for tracking the creation and update time are also included.
    """

    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """Save the model instance."""
        if not self.slug:
            self.slug = self.generate_slug()

        super().save(*args, **kwargs)

    def generate_slug(self):
        """
        Generate a unique slug for the model instance.
        """
        raise NotImplementedError("Method 'generate_slug' must be implemented in a subclass.")


class SortableModel(TimeStampedModel):
    """
    An abstract base class model that provides a ``position`` field.
    The timestamp fields for tracking the creation and update time are also included.
    """

    position = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
