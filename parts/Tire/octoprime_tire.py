from parts.Tire.tire import Tire
"""Modifying the behavior of a part for all cars which
contain that part can be accomplished by modifying a
single piece of code. """


class OctoprimeTire(Tire):
    tire_wear = list[float]
   
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        if sum(self.tire_wear) >= 3:
            return True
        else:
            return False
