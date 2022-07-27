from djongo import models
from rest_framework_api_key.crypto import KeyGenerator, concatenate

class APIKeyManager(models.DjongoManager):
    key_generator = KeyGenerator()

    def assign_key(self,obj):
        key,prefix,hashed_key = self.key_generator.generate()
        pk = concatenate(prefix,hashed_key)

        obj.id = pk
        obj.prefix = prefix
        obj.hashed_key = hashed_key

        return key
    
    def create_key(self, **kwargs):
        # Prevent from manually setting the primary key.
        kwargs.pop("id", None)
        obj = self.model(**kwargs)
        key = self.assign_key(obj)
        obj.save()
        return obj, key

    def get_usable_keys(self) -> models.QuerySet:
        return self.all()

    def get_from_key(self, key: str):
        prefix, _, _ = key.partition(".")
        queryset = self.get_usable_keys()

        try:
            api_key = queryset.get(prefix=prefix)
        except self.model.DoesNotExist:
            raise  # For the sake of being explicit.

        if not api_key.is_valid(key):
            raise self.model.DoesNotExist("Key is not valid.")
        else:
            return api_key

    def is_valid(self, key: str) -> bool:
        try:
            api_key = self.get_from_key(key)
        except self.model.DoesNotExist:
            return False

        return True