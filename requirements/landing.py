from requirements.area import Area
from requirements.requirement import Requirement


class Landing(Requirement):

    def __init__(self, i, a):
        super().__init__(i)
        self.area = Area(a)

    def update_on_land(self, x, y, z):

        if self.area.contains(x, y, z):
            super().complete()
