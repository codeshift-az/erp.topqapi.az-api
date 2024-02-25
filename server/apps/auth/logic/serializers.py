from rest_framework import serializers


class TokenPairSerializer(serializers.Serializer):
    """Serializer for token pair."""

    access = serializers.CharField()
    refresh = serializers.CharField()


class AccessTokenSerializer(serializers.Serializer):
    """Serializer for access token."""

    access = serializers.CharField()
