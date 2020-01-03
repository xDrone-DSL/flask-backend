from requirements.area import Area
from requirements.requirement import Requirement


class Avoidance(Requirement):

    def __init__(self, i, a):
        super().__init__(i)

        super().complete()
        self.area = Area(a)

    def update_on_move(self, x, y, z):

        if self.area.contains(x, y, z):
            super().fail()
