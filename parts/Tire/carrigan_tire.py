from parts.Tire.tire import Tire
"""Modifying the behavior of a part for all cars which
contain that part can be accomplished by modifying a
single piece of code. """


class CarriganTire(Tire):
    tire_wear = list[float]
   
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        for x in self.tire_wear:
            if x >= 0.9:
                return True
        return False
