
class Area:

    def __init__(self, z):
        self.x_low = min(z["x_low"], z["x_high"])
        self.x_high = max(z["x_low"], z["x_high"])

        self.y_low = min(z["y_low"], z["y_high"])
        self.y_high = max(z["y_low"], z["y_high"])

        self.z_low = min(z["z_low"], z["z_high"])
        self.z_high = max(z["z_low"], z["z_high"])

    def contains(self, x, y, z):
        return self.x_low <= x <= self.x_high and \
               self.y_low <= y <= self.y_high and \
               self.z_low <= z <= self.z_high
