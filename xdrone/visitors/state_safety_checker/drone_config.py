import copy


class DroneConfig:
    def __init__(self, speed_mps: float, rotate_speed_dps: float, takeoff_height_meters: float):
        if speed_mps <= 0:
            raise ValueError("speed_mps should > 0")
        if rotate_speed_dps <= 0:
            raise ValueError("rotate_speed_dps should > 0")
        if takeoff_height_meters <= 0:
            raise ValueError("takeoff_height_meters should > 0")
        self._speed_mps = speed_mps
        self._rotate_speed_dps = rotate_speed_dps
        self._takeoff_height_meters = takeoff_height_meters

    @property
    def speed_mps(self) -> float:
        return copy.deepcopy(self._speed_mps)

    @property
    def rotate_speed_dps(self) -> float:
        return copy.deepcopy(self._rotate_speed_dps)

    @property
    def takeoff_height_meters(self) -> float:
        return copy.deepcopy(self._takeoff_height_meters)

    def __str__(self):
        return ("DroneConfig: {{ speed_mps: {}, rotate_speed_dps: {}, takeoff_height_meters: {} }}"
                .format(self._speed_mps, self._rotate_speed_dps, self._takeoff_height_meters))

    def __eq__(self, other):
        if isinstance(other, DroneConfig):
            return other._speed_mps == self._speed_mps and other._rotate_speed_dps == self._rotate_speed_dps \
                   and other._takeoff_height_meters == self._takeoff_height_meters
        return False


class DefaultDroneConfig(DroneConfig):
    def __init__(self):
        super().__init__(speed_mps=1, rotate_speed_dps=90, takeoff_height_meters=1)
