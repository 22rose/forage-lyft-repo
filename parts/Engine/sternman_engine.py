from parts.Engine.engine import Engine
"""Modifying the behavior of a part for all cars which
contain that part can be accomplished by modifying a
single piece of code. """


class SternmanEngine(Engine):
    warning_light_on: bool

    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        if self.warning_light_on:
            return True
        else:
            return False
