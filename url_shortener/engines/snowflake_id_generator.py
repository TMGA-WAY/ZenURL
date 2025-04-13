import time
import threading


class SnowflakeIdGenerator:
    def __init__(self, machine_id: int = 1, datacenter_id: int = 1):
        self.machine_id = machine_id & 0x1F
        self.datacenter_id = datacenter_id & 0x1F
        self.sequence = 0
        self.last_timestamp = -1
        self.lock = threading.Lock()

    def _current_time_millis(self):
        return int(time.time() * 1000)

    def _wait_next_millis(self, last_timestamp):
        timestamp = self._current_time_millis()
        while timestamp <= last_timestamp:
            timestamp = self._current_time_millis()
        return timestamp

    def create_id(self):
        # Get the current timestamp in milliseconds
        with self.lock:
            timestamp = self._current_time_millis()

            if timestamp < self.last_timestamp:
                raise Exception("Clock moving backwards")

            if timestamp == self.last_timestamp:
                self.sequence = (self.sequence + 1) & 0xFFF  # 4095
                if self.sequence == 0:
                    timestamp = self._wait_next_millis(self.last_timestamp)
            else:
                self.sequence = 0

            self.last_timestamp = timestamp

            uuid = (
                    (timestamp << 22) |
                    (self.datacenter_id << 17) |
                    (self.machine_id << 12) |
                    self.sequence
            )

            return uuid
