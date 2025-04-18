import datetime as dt

from pymongo.synchronous.cursor import Cursor

from ..db.mongo_connection import MongoDBConnection
from ..engines.base64_generator import Base64Generator
from ..engines.md_5_encryptor import MD5Encryptor
from ..engines.snowflake_id_generator import SnowflakeIdGenerator
from ..schema.long_url_serializer import ShortUrlSerializer
from ..util import constant as const


def get_long_url(short_url, user_id=None):
    """
    Retrieve the long URL associated with the given short URL.
    :param short_url: The short URL to be expanded.
    :param user_id: The ID of the user requesting the long URL (optional).
    :return: The long URL if found, otherwise None.
    """
    db_connection = MongoDBConnection()
    document = {
        "short_url": short_url
    }
    res = db_connection.get_collection_by_condition(collection_name=const.URL_COLLECTION_NAME,
                                                    query=document)
    res = list(res)
    if not res:
        return
    return res[0]["long_url"]


def create_short_url(long_url: str, extra_small: bool = False, user_id: int | None = None, is_public: bool = True):
    """
    Create a short URL for the given long URL.
    :param extra_small: True if the short URL should be tiny as possible (default: False).
    :param long_url: The long URL to be shortened.
    :param user_id: The ID of the user creating the short URL (optional).
    :param is_public: Whether the short URL should be public or not (default: True).
    :return: The created short URL.
    """
    # Validate the long URL

    # Todo: Get machine_id and datacenter_id from config

    document = {
        "long_url": long_url  # Todo: Add user_id and is_public to the document
    }

    db_connection = MongoDBConnection()
    res = db_connection.get_collection_by_condition(collection_name=const.URL_COLLECTION_NAME, query=document)
    res = list(res)
    short_url = None

    if not res:
        # If the long URL does not exist, create a new short URL
        snowflake_id_generator = SnowflakeIdGenerator()
        base64_converter = Base64Generator()

        if extra_small:
            # Generate a new short URL using the MD5 hash
            md5_hash = MD5Encryptor()

            for _ in range(100):

                # To resolve the collision, we need to generate a new hash
                unique_id = md5_hash.create_hash(long_url, snowflake_id_generator.create_id())
                short_url = base64_converter.encode(unique_id)[:8]

                # Check if the short URL already exists
                res = db_connection.get_collection_by_condition(
                    collection_name=const.URL_COLLECTION_NAME,
                    query={"short_url": short_url,
                           "long_url": {"$ne": long_url}
                           }
                )

                if isinstance(res, Cursor):
                    # If the short URL is unique, break the loop
                    break

            if not short_url:
                raise "Unable to generate a unique short URL after 100 attempts."
        else:
            # Generate a new short URL using the Snowflake ID generator
            unique_id = snowflake_id_generator.create_id()
            short_url = base64_converter.encode(unique_id)

        db_connection.insert_document(const.URL_COLLECTION_NAME, {"short_url": short_url,
                                                                  "created_at": dt.datetime.utcnow(),
                                                                  **document})
    else:
        # If the long URL already exists, use the existing short URL
        short_url = res[0]["short_url"]

    short_url_serializer = ShortUrlSerializer(data={"long_url": long_url, "short_url": short_url})

    if not short_url_serializer.is_valid():
        return short_url_serializer.errors

    return short_url_serializer.data
