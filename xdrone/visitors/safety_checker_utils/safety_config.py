from xdrone.visitors.safety_checker_utils.safety_check_error import SafetyCheckError
from xdrone.visitors.safety_checker_utils.status import Status


class SafetyConfig:
    def __init__(self, max_seconds: float = 0,
                 max_x_meters: float = 0, max_y_meters: float = 0, max_z_meters: float = 0,
                 min_x_meters: float = 0, min_y_meters: float = 0, min_z_meters: float = 0):
        if max_seconds < 0:
            raise ValueError("max_seconds should >= 0")
        if max_x_meters < min_x_meters:
            raise ValueError("max_x_meters should >= min_x_meters")
        if max_y_meters < min_y_meters:
            raise ValueError("max_y_meters should >= min_y_meters")
        if max_z_meters < min_z_meters:
            raise ValueError("max_z_meters should >= min_z_meters")
        self._max_seconds = max_seconds
        self._max_x_meters = max_x_meters
        self._max_y_meters = max_y_meters
        self._max_z_meters = max_z_meters
        self._min_x_meters = min_x_meters
        self._min_y_meters = min_y_meters
        self._min_z_meters = min_z_meters

    def __str__(self):
        return ("SafetyConfig: {{ max_seconds: {}, x_range_meters: {}, y_range_meters: {}, z_range_meters: {} }}"
                .format(self._max_seconds, (self._min_x_meters, self._max_x_meters),
                        (self._min_y_meters, self._max_y_meters), (self._min_z_meters, self._max_z_meters)))

    def __eq__(self, other):
        if isinstance(other, SafetyConfig):
            return other._max_seconds == self._max_seconds and other._max_x_meters == self._max_x_meters \
                   and other._max_y_meters == self._max_y_meters and other._max_z_meters == self._max_z_meters \
                   and other._min_x_meters == self._min_x_meters and other._min_y_meters == self._min_y_meters \
                   and other._min_z_meters == self._min_z_meters
        return False

    def check_status(self, status: Status):
        if status.x_meters > self._max_x_meters:
            raise SafetyCheckError("The x coordinate {} will go beyond its upper limit {}"
                                   .format(status.x_meters, self._max_x_meters))
        if status.y_meters > self._max_y_meters:
            raise SafetyCheckError("The y coordinate {} will go beyond its upper limit {}"
                                   .format(status.y_meters, self._max_y_meters))
        if status.z_meters > self._max_z_meters:
            raise SafetyCheckError("The z coordinate {} will go beyond its upper limit {}"
                                   .format(status.z_meters, self._max_z_meters))
        if status.x_meters < self._min_x_meters:
            raise SafetyCheckError("The x coordinate {} will go beyond its lower limit {}"
                                   .format(status.x_meters, self._min_x_meters))
        if status.y_meters < self._min_y_meters:
            raise SafetyCheckError("The y coordinate {} will go beyond its lower limit {}"
                                   .format(status.y_meters, self._min_y_meters))
        if status.z_meters < self._min_z_meters:
            raise SafetyCheckError("The z coordinate {} will go beyond its lower limit {}"
                                   .format(status.z_meters, self._min_z_meters))
        if status.time_used_seconds > self._max_seconds:
            raise SafetyCheckError("The time used {} seconds will go beyond the time limit {} seconds"
                                   .format(status.time_used_seconds, self._max_seconds))
