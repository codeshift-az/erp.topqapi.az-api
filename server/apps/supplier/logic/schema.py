from drf_spectacular.extensions import OpenApiSerializerFieldExtension
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.plumbing import build_basic_type
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import Direction

from server.apps.supplier.logic.serializers import SupplierSerializer


class SupplierFieldSchema(OpenApiSerializerFieldExtension):
    target_class = "server.apps.supplier.logic.fields.SupplierField"

    def map_serializer_field(self, auto_schema: AutoSchema, direction: Direction):
        if direction == "request":
            return build_basic_type(OpenApiTypes.INT)

        return auto_schema.resolve_serializer(SupplierSerializer, direction).ref
