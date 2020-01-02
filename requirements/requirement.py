class Requirement:

    def __init__(self, i):
        self.id = i
        self.completed = False

    def is_completed(self):
        return self.completed

    def complete(self):
        self.completed = True

    def fail(self):
        self.completed = False

    def get_id(self):
        return self.id

    def update_on_move(self, x, y, z):
        pass

    def update_on_action(self, x, y, z):
        pass

    def update_on_land(self, x, y, z):
        pass
