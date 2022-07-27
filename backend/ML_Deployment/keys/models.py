from djongo import models

from .managers import APIKeyManager


class APIKey(models.Model):

    objects = APIKeyManager()

    id = models.CharField(max_length=150, unique=True, primary_key=True, editable=False)
    prefix = models.CharField(max_length=8, unique=True, editable=False)
    hashed_key = models.CharField(max_length=150, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    name = models.CharField(
        max_length=50,
        blank=False,
        default=None,
        help_text=(
            "A free-form name for the API key. "
            "Need not be unique. "
            "50 characters max."
        ),
    )

    def is_valid(self, key: str) -> bool:
        return type(self).objects.key_generator.verify(key, self.hashed_key)

    def __str__(self) -> str:
        return str(self.name)
