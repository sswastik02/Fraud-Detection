import typing

from django.contrib import admin, messages
from django.db import models
from django.http.request import HttpRequest

from .models import APIKey


class APIKeyModelAdmin(admin.ModelAdmin):
    model=APIKey

    list_display = (
        "prefix",
        "name",
        "created",
    )
    list_filter = ("created",)
    search_fields = ("name", "prefix")

    def save_model(
        self,
        request: HttpRequest,
        obj: APIKey,
        form: typing.Any = None,
        change: bool = False,
    ) -> None:
        created = not obj.pk

        if created:
            key = self.model.objects.assign_key(obj)
            obj.save()
            message = (
                "The API key for {} is: {}. ".format(obj.name, key)
                + "Please store it somewhere safe: "
                + "you will not be able to see it again."
            )
            messages.add_message(request, messages.WARNING, message)
        else:
            obj.save()


admin.site.register(APIKey, APIKeyModelAdmin)

APIKeyAdmin = APIKeyModelAdmin  # Compatibility with <1.3
