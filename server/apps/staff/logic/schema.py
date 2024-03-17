from drf_spectacular.extensions import OpenApiSerializerFieldExtension
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.plumbing import build_basic_type
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import Direction

from server.apps.staff.logic.serializers import DriverSerializer, SellerSerializer, WorkerSerializer


class DriverFieldSchema(OpenApiSerializerFieldExtension):
    target_class = "server.apps.staff.logic.fields.DriverField"

    def map_serializer_field(self, auto_schema: AutoSchema, direction: Direction):
        if direction == "request":
            return build_basic_type(OpenApiTypes.INT)

        return auto_schema.resolve_serializer(DriverSerializer, direction).ref


class SellerFieldSchema(OpenApiSerializerFieldExtension):
    target_class = "server.apps.staff.logic.fields.SellerField"

    def map_serializer_field(self, auto_schema: AutoSchema, direction: Direction):
        if direction == "request":
            return build_basic_type(OpenApiTypes.INT)

        return auto_schema.resolve_serializer(SellerSerializer, direction).ref


class WorkerFieldSchema(OpenApiSerializerFieldExtension):
    target_class = "server.apps.staff.logic.fields.WorkerField"

    def map_serializer_field(self, auto_schema: AutoSchema, direction: Direction):
        if direction == "request":
            return build_basic_type(OpenApiTypes.INT)

        return auto_schema.resolve_serializer(WorkerSerializer, direction).ref
