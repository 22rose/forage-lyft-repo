from parts.Battery.battery import Battery
from datetime import date, timedelta
"""Modifying the behavior of a part for all cars which
contain that part can be accomplished by modifying a
single piece of code. """


class NubbinBattery(Battery):
    last_service_date: date
    current_date: date

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        four_years = timedelta(days=365 * 4)
        if self.current_date - self.last_service_date >= four_years:
            return True
        else:
            return False
