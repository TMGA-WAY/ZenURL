import hashlib


class MD5Encryptor:

    def create_hash(self, url: str, snowflake_id) -> bytes:
        """
        Create an MD5 hash of the given URL.

        :param snowflake_id:
        :param url: The URL to be hashed.
        :return: The MD5 hash of the URL.
        """
        salt = self.get_random_salt(snowflake_id)
        salted_url = f"{url}{salt}"
        md5_hash = hashlib.md5(salted_url.encode()).digest()
        return md5_hash

    def get_random_salt(self, snowflake_id) -> str:
        """
        Generate a random salt based on the snowflake ID.

        :param snowflake_id: The snowflake ID to be used for generating the salt.
        :return: The generated salt.
        """
        return str(snowflake_id)[-7:]
