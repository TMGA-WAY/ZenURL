from zenurl.url_shortener.engines.base64_generator import Base62Encoder
from zenurl.url_shortener.engines.snowflake_id_generator import SnowflakeIdGenerator


def create_short_url(long_url: str, user_id: str = None) -> str:
    try:
        # TODO: First check the long_url is present or not, if user_id is there, then filter with user id

        # Generate Snowflake ID
        snowflake_id_generator = SnowflakeIdGenerator()
        snowflake_id = snowflake_id_generator.next_id(datacenter_id=1, machine_id=1)

        if not snowflake_id:
            return _exception_message()

        # Generate Base64 String
        base62_string = Base62Encoder(snowflake_id=snowflake_id)
        if not base62_string:
            return _exception_message()

        # TODO: Call models to store the value
        saved = False
        # saved = # Store it in model
        if not saved:
            _exception_message()
        return str(base62_string)

    except Exception as e:
        print("Exception occurred \t", e)
        return _exception_message()


def fetch_long_url(short_url: str, user_id: str | None) -> str:
    try:
        # TODO: Call model to get long_url
        long_url = "Call the model to fetch long_url; make sure user permission is true"

        if long_url == '401':
            return _url_not_found(status_code=long_url)
        if long_url == '404':
            return _url_not_found(status_code=long_url)

        return long_url
    except Exception as e:
        print("Exception occurred \t", e)
        return _exception_message()


def _exception_message() -> str:
    return "Please Check the URL is valid or not and try again."


def _url_not_found(status_code: str) -> str:
    return "You do not have permission to see the URL"
