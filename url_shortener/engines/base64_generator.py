from collections import deque

CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Base62Encoder:
    def __init__(self, snowflake_id):
        self.id = snowflake_id

    def get_base64_string(self) -> str | None:
        try:
            base64 = deque()
            while self.id:
                self.id, rem = divmod(self.id, 62)
                base64.appendleft(CHARS[rem])

            return ''.join(base64)
        except Exception as e:
            print("Exception in Base64 \t", e)
            return None
