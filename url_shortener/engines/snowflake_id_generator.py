import time


def _current_millis():
    return round(time.time() * 1000)


class SnowflakeIdGenerator:
    def __init__(self, epochs=1735689600000):
        self.epoch = epochs
        self.sequence = 0
        self.last_timestamp = -1

    def next_id(self, datacenter_id=1, machine_id=1) -> int | None:
        try:
            timestamp = _current_millis()

            if timestamp == self.last_timestamp:
                self.sequence = (self.sequence + 1) & 0xFFF
                if self.sequence == 0:
                    while timestamp <= self.last_timestamp:
                        timestamp = _current_millis()
            else:
                self.sequence = 0

            self.last_timestamp = timestamp

            snowflake_unique_id = ((timestamp - self.epoch) << 22) | (datacenter_id << 17) | (
                    machine_id << 12) | self.sequence
            return snowflake_unique_id
        except Exception as e:
            print("Exception in SnowflakeIdGenerator \t", e)
            return None
