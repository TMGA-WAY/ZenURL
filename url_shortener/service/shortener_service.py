from ..engines.base64_generator import Base62Encoder
from ..engines.snowflake_id_generator import SnowflakeIdGenerator
from ..models import Url


def save_short_url(long_url: str, user_id: str = None, is_public: bool = True) -> str:
    try:
        # TODO: First check the long_url is present or not, if user_id is there, then filter with user id
        print("inside save_short_url")
        fetched_url = _find_url(url=long_url, user_id=user_id, is_long_url=True)
        print("fetched_url", fetched_url)
        if fetched_url != any({'404', '401'}):
            return fetched_url

        # Generate Snowflake ID
        snowflake_id_generator = SnowflakeIdGenerator()
        snowflake_id = snowflake_id_generator.next_id(datacenter_id=1, machine_id=1)
        print("snowflake_id", snowflake_id)
        if not snowflake_id:
            return _exception_message()

        # Generate Base64 String
        base62_string = Base62Encoder(snowflake_id=snowflake_id)
        if not base62_string:
            return _exception_message()
        print("base62_string", base62_string)
        # TODO: Call models to store the value
        url = Url.objects.create(short_url=str(base62_string),
                                 long_url=long_url,
                                 user_id=user_id,
                                 is_public=is_public)

        url.save()
        return str(base62_string)

    except Exception as e:
        print("Exception occurred \t", e)
        return _exception_message()


def fetch_url(url: str, user_id: str | None, is_long=True) -> str:
    try:
        # TODO: Call model to get long_url
        url_status_string = _find_url(url=url,
                                      user_id=user_id,
                                      is_long_url=is_long)

        if url_status_string == '401':
            return _url_permission_denied(status_code=url_status_string)
        if url_status_string == '404':
            return _url_not_found(status_code=url_status_string)

        return url_status_string
    except Exception as e:
        print("Exception occurred \t", e)
        return _exception_message()


def _find_url(url: str, user_id: str | None, is_long_url: bool = True) -> str:
    """ Internal function to fetch the URL based on the user_id and/or is_long_url """
    try:
        if is_long_url:
            # Todo: call model to fetch long_url
            url_instances = Url.objects.filter(long_url=url)
            if not url_instances:  # If not found, then return 404
                return '404'
        else:
            url_instances = Url.objects.filter(short_url=url)
            if not url_instances:
                return '404'

        if user_id and url_instances.get("user_id", None) != user_id:
            return '401'
        elif url_instances.get("is_public", None) != False:
            return '401'

        return url_instances

        return url_instances
    except Exception as e:
        print("Exception occurred \t", e)
        return _exception_message()


def _exception_message() -> str:
    """ Internal function to return the exception message """
    return "Please Check the URL is valid or not and try again."


def _url_permission_denied(status_code: str) -> str:
    """ Internal function to return the permission denied message """
    return "You do not have permission to see the URL"


def _url_not_found(status_code: str) -> str:
    """ Internal function to return the URL not found message """
    return "Requested URL is not found"
