BASE64_URL_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_+"


class Base64Generator:

    def base64_generator(self, url_id):
        if url_id == 0:
            yield BASE64_URL_ALPHABET[0]
        else:
            while url_id > 0:
                url_id, rem = divmod(url_id, 64)
                yield BASE64_URL_ALPHABET[rem]

    def encode(self, url_id) -> str:
        return ''.join(self.base64_generator(url_id))[::-1]

    def decode(self, short_url: str) -> int:
        base_id = 0
        for char in short_url:
            base_id = base_id * 64 + BASE64_URL_ALPHABET.index(char)
        return base_id
