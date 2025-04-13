from rest_framework import serializers


class LongUrlSerializer(serializers.Serializer):
    """
    Serializer for the long URL.
    """
    url = serializers.CharField(max_length=2000, required=True)

    def validate_long_url(self, value):
        """
        Validate the long URL.
        """
        if not value.startswith("http://") and not value.startswith("https://"):
            raise serializers.ValidationError("Invalid URL format. URL must start with 'http://' or 'https://'.")
        return value


class ShortUrlSerializer(serializers.Serializer):
    """
    Serializer for the short URL.
    """
    short_url = serializers.CharField(max_length=255, required=True)
    long_url = serializers.CharField(max_length=2000, required=True)
