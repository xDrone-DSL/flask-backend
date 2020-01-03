from requirements.requirement import Requirement
from requirements.area import Area


class Action(Requirement):

    def __init__(self, i, a):
        super().__init__(i)

        self.area = Area(a)

    def update_on_action(self, x, y, z):
        if self.area.contains(x, y, z):
            super().complete()
