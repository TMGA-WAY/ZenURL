from ..engines.base64_generator import Base64Generator
from ..engines.snowflake_id_generator import SnowflakeIdGenerator
from ..schema.long_url_serializer import ShortUrlSerializer


def create_short_url(long_url, user_id=None, is_public=True):
    """
    Create a short URL for the given long URL.
    :param long_url: The long URL to be shortened.
    :param user_id: The ID of the user creating the short URL (optional).
    :param is_public: Whether the short URL should be public or not (default: True).
    :return: The created short URL.
    """
    # Validate the long URL

    # Todo: Get machine_id and datacenter_id from config

    snowflake_id_generator = SnowflakeIdGenerator()
    base64_converter = Base64Generator()

    unique_id = snowflake_id_generator.create_id()
    short_url = base64_converter.encode(unique_id)

    short_url_serializer = ShortUrlSerializer(data={"long_url": long_url, "short_url": short_url})

    if not short_url_serializer.is_valid():
        return short_url_serializer.errors

    return short_url_serializer.data
