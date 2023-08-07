import unittest
from datetime import date
from cars.car_factory import CarFactory
from cars.car import Car


class TestCarFactory(unittest.TestCase):
    def test_create_calliope(self):
        current_date = date(2023, 8, 1)
        last_service_date = date(2022, 8, 1)
        current_mileage = 50000
        last_service_mileage = 40000
        tire_wear = [0.1, 0.3, 0.4, 0.8]

        car = CarFactory.create_calliope(current_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_wear)
        self.assertIsInstance(car, Car)

    def test_create_glissade(self):
        current_date = date(2023, 8, 1)
        last_service_date = date(2022, 8, 1)
        current_mileage = 50000
        last_service_mileage = 40000
        tire_wear = [0.1, 0.3, 0.4, 0.8]

        car = CarFactory.create_glissade(current_date, last_service_date,
                                         current_mileage, last_service_mileage, tire_wear)
        self.assertIsInstance(car, Car)
    
    def test_create_palindrome(self):
        current_date = date(2023, 8, 1)
        last_service_date = date(2022, 8, 1)
        warning_light_on = True
        tire_wear = [0.1, 0.3, 0.4, 0.8]

        car = CarFactory.create_palindrome(current_date, last_service_date,
                                           warning_light_on, tire_wear)
        self.assertIsInstance(car, Car)
    
    def test_create_rorschach(self):
        current_date = date(2023, 8, 1)
        last_service_date = date(2022, 8, 1)
        current_mileage = 50000
        last_service_mileage = 40000
        tire_wear = [0.1, 0.3, 0.4, 0.8]

        car = CarFactory.create_rorschach(current_date, last_service_date,
                                          current_mileage,
                                          last_service_mileage, tire_wear)
        self.assertIsInstance(car, Car)
    
    def test_create_thovex(self):
        current_date = date(2023, 8, 1)
        last_service_date = date(2022, 8, 1)
        current_mileage = 50000
        last_service_mileage = 40000
        tire_wear = [0.1, 0.3, 0.4, 0.8]

        car = CarFactory.create_thovex(current_date, last_service_date,
                                       current_mileage, last_service_mileage, tire_wear)
        self.assertIsInstance(car, Car)
