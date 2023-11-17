import uuid

from django.db import models


class TimeStampedUUIDModel(models.Model):
    """
    An abstract base class model that provides UUID field and self updating
    ``created_at`` and ``updated_at``.
    """
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
