class Status:
    def __init__(self, has_taken_off: bool, time_used_seconds: float = 0,
                 x_meters: float = 0, y_meters: float = 0, z_meters: float = 0, orientation_degrees: float = 0):
        self.has_taken_off = has_taken_off
        self.time_used_seconds = time_used_seconds
        self.x_meters = x_meters
        self.y_meters = y_meters
        self.z_meters = z_meters
        self.orientation_degrees = orientation_degrees

    def __str__(self):
        return ("Status: {{ has_taken_off: {}, time_used_seconds: {}, "
                .format(self.has_taken_off, self.time_used_seconds) +
                "x_meters: {}, y_meters: {}, z_meters: {}, orientation_degrees: {} }}"
                .format(self.x_meters, self.y_meters, self.z_meters, self.orientation_degrees))

    def __eq__(self, other):
        if isinstance(other, Status):
            return other.has_taken_off == self.has_taken_off and other.time_used_seconds == self.time_used_seconds \
                   and other.x_meters == self.x_meters and other.y_meters == self.y_meters \
                   and other.z_meters == self.z_meters and other.orientation_degrees == self.orientation_degrees
        return False
