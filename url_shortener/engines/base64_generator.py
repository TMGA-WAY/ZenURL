BASE64_URL_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-"


class Base64Generator:
    def _int_to_base64(self, url_id):
        if url_id == 0:
            return BASE64_URL_ALPHABET[0]
        else:
            base64_str = ""
            while url_id > 0:
                url_id, rem = divmod(url_id, 64)
                base64_str += BASE64_URL_ALPHABET[rem]
            return base64_str[::-1]

    def encode(self, url_id):
        if isinstance(url_id, int):
            # we need to convert it to base64
            return self._int_to_base64(url_id)

        # url_id is a byte object
        big_int = int.from_bytes(url_id, 'big')
        return self._int_to_base64(big_int)
