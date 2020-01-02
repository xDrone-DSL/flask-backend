from requirements.area import Area
from requirements.requirement import Requirement


class ContinuousAction(Requirement):

    def __init__(self, i, a1, a2):
        super().__init__(i)

        self.area_1 = Area(a1)
        self.area_2 = Area(a2)
        self.in_progress = False
        self.started_in_area_1 = False

    def update_on_action(self, x, y, z):
        if not self.in_progress:

            if self.area_1.contains(x, y, z):
                self.in_progress = True
                self.started_in_area_1 = True

            elif self.area_2.contains(x, y, z):
                self.in_progress = True
                self.started_in_area_1 = False

        else:
            # Action is therefore in progress

            if self.started_in_area_1 and self.area_2.contains(x, y, z):
                super().complete()
            elif not self.started_in_area_1 and self.area_1.contains(x, y, z):
                super().complete()

            self.in_progress = False
