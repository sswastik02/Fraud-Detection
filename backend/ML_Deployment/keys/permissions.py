from rest_framework import permissions
from rest_framework_api_key.permissions import KeyParser

from .models import APIKey

class HasAPIKey(permissions.BasePermission):
    model = APIKey
    key_parser = KeyParser()

    def get_key(self, request):
        return self.key_parser.get(request)

    def has_permission(self, request, view) -> bool:
        assert self.model is not None, (
            "%s must define `.model` with the API key model to use"
            % self.__class__.__name__
        )
        key = self.get_key(request)
        if not key:
            return False
        return self.model.objects.is_valid(key)

    def has_object_permission(
        self, request, view, obj
    ) -> bool:
        return self.has_permission(request, view)