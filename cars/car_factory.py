from datetime import date
from cars.car import Car
from parts.Engine.capulet_engine import CapuletEngine
from parts.Engine.sternman_engine import SternmanEngine
from parts.Engine.willoughby_engine import WilloughbyEngine
from parts.Battery.spindler_battery import SpindlerBattery
from parts.Battery.nubbin_battery import NubbinBattery
from parts.Tire.carrigan_tire import CarriganTire
from parts.Tire.octoprime_tire import OctoprimeTire

"""Changing the parts a car is
composed of can be accomplished
by modifying the corresponding"""

"""Cars are created by calling the
corresponding create method on car_factory"""


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int, tire_wear: list[float]):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int, tire_wear: list[float]):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTire(tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date,
                          warning_light_on: bool, tire_wear: list[float]):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date,
                         current_mileage: int, last_service_mileage: int, tire_wear: list[float]):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTire(tire_wear)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, 
                      current_mileage: int, last_service_mileage: int, tire_wear: list[float]):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear)
        return Car(engine, battery, tires)
