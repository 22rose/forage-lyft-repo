from parts.Engine.engine import Engine
"""Modifying the behavior of a part for all cars which
contain that part can be accomplished by modifying a
single piece of code."""


class WilloughbyEngine(Engine):
    last_service_mileage: int
    current_mileage: int

    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= 60000
