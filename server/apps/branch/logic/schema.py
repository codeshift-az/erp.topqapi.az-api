from drf_spectacular.extensions import OpenApiSerializerFieldExtension
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.plumbing import build_basic_type
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import Direction

from server.apps.branch.logic.serializers import BranchSerializer


class BranchFieldSchema(OpenApiSerializerFieldExtension):
    target_class = "server.apps.branch.logic.fields.BranchField"

    def map_serializer_field(self, auto_schema: AutoSchema, direction: Direction):
        if direction == "request":
            return build_basic_type(OpenApiTypes.INT)

        return auto_schema.resolve_serializer(BranchSerializer, direction).ref
