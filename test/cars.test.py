import unittest
from datetime import date
from cars.car_factory import CarFactory


class TestCarNeedsService(unittest.TestCase):
    def test_calliope_battery_needs_service(self):
        car = CarFactory.create_calliope(date(2023, 8, 1), date(2020, 8, 1), 50000, 40000, [0.1, 0.1, 0.1, 0.1])
        self.assertTrue(car.needs_service())  #battery needs service because its greater
        #or equal to three years
        #engine does not need service
        #tires do not need service
    
    def test_calliope_engine_needs_service(self):
        car = CarFactory.create_calliope(date(2023, 8, 1), date(2022, 8, 1), 90000, 40000, [0.1, 0.1, 0.1, 0.1])
        self.assertTrue(car.needs_service())  #battery does not need service because its less than 3 years
        #engine needs service because mileage difference is greater than 30000
        #tires do not need service
    
    def test_calliope_tires_needs_service(self):
        car = CarFactory.create_calliope(date(2023, 8, 1), date(2022, 8, 1), 50000, 40000, [0.1, 0.1, 0.9, 0.1])
        self.assertTrue(car.needs_service()) # #battery does not need service because its less than 3 years
        #engine does not need service because mileage difference is less than 30000
        #tires need service cause one is 0.9

    def test_calliope_does_not_need_service(self):
        car = CarFactory.create_calliope(date(2023, 8, 1), date(2022, 8, 1), 45000, 40000, [0.1, 0.1, 0.1, 0.1])
        self.assertFalse(car.needs_service()) #does not need service because its less than 
        #three years and mileage difference is less than 30000 and none of the tires are 
        #greater than 0.9

    def test_glissade_battery_needs_service(self):
        car = CarFactory.create_glissade(date(2023, 8, 1), date(2019, 8, 1), 50000, 40000, [0.1, 0.2, 0.3, 0.5])
        self.assertTrue(car.needs_service())  #battery needs service because its greater than three years
        #engine does not need service  #tires does not need service cause sum is not greater than 3
    
    def test_glissade_engine_needs_service(self):
        car = CarFactory.create_glissade(date(2023, 8, 1), date(2022, 8, 1), 110000, 40000, [0.1, 0.2, 0.3, 0.5])
        self.assertTrue(car.needs_service())  #battery does not need service because its less than 3 years
        #engine needs service because 110000 - 40000 >= 60000
        #tires does not need service cause sum is not greater than 3
    
    def test_glissade_tires_needs_service(self):
        car = CarFactory.create_glissade(date(2023, 8, 1), date(2022, 8, 1), 50000, 40000, [0.9, 0.9, 0.9, 0.9])
        self.assertTrue(car.needs_service()) #battery does not need service because its less than 3 years
        #engine does not need service #tires need service cause sum is greater than 3

    def test_glissade_does_not_need_service(self):
        car = CarFactory.create_glissade(date(2023, 8, 1), date(2022, 8, 1), 45000, 40000, [0.1, 0.2, 0.3, 0.5])
        self.assertFalse(car.needs_service())  #does not need service because its less than 
        #three years and mileage difference is less than 60000
        #tires does not need service cause sum is not greater than 3
    
    def test_palindrome_battery_needs_service(self):
        car = CarFactory.create_palindrome(date(2023, 8, 1), date(2018, 8, 1), False, [0.1, 0.8, 0.3, 0.5])
        self.assertTrue(car.needs_service())  #battery needs service because its greater than three years
        #engine does not need service #tires do not need service cause none is 0.9 or greater
    
    def test_palindrome_engine_needs_service(self):
        car = CarFactory.create_palindrome(date(2023, 8, 1), date(2022, 8, 1), True, [0.1, 0.8, 0.3, 0.5])
        self.assertTrue(car.needs_service())  #battery needs service because its less than 3 years
        #engine needs service because warning light is on (true)
        #tires do not need service cause none is 0.9 or greater
    
    def test_palindrome_tires_need_service(self):
        car = CarFactory.create_palindrome(date(2023, 8, 1), date(2022, 8, 1), False, [0.1, 0.9, 0.3, 0.5])
        self.assertTrue(car.needs_service())  #battery does not need service because its less
        #than three years
        #engine does not need service because warning light is off (false)
        #tires need service cause at least one is 0.9 or greater

    
    def test_palindrome_does_not_need_service(self):
        car = CarFactory.create_palindrome(date(2023, 8, 1), date(2022, 8, 1), False, [0.1, 0.8, 0.3, 0.5])
        self.assertFalse(car.needs_service())  #battery does not need service because its less
        #than three years
        #engine does not need service because warning light is off (false)
        #tires do not need service cause none is 0.9 or greater
        
    def test_rorschach_battery_needs_service(self):
        car = CarFactory.create_rorschach(date(2023, 8, 1), date(2016, 8, 1), 80000, 75000, [0.1, 0.2, 0.3, 0.5])
        self.assertTrue(car.needs_service()) #battery needs service cause its greater than 4 years
        #engine does not need service because the mileage difference is less than 60000
        #tires do not need service cause sum is not greater than 3
    
    def test_rorschach_engine_needs_service(self):
        car = CarFactory.create_rorschach(date(2023, 8, 1), date(2022, 8, 1), 80000, 10000, [0.1, 0.2, 0.3, 0.5])
        self.assertTrue(car.needs_service()) #battery does not need service because its less than 4 years
        #engine needs service cause mileage difference is greater than 60000
        #tires do not need service cause sum is not greater than 3
    
    def test_rorschach_tires_needs_service(self):
        car = CarFactory.create_rorschach(date(2023, 8, 1), date(2022, 8, 1), 80000, 75000, [0.9, 0.9, 0.9, 0.9])
        self.assertTrue(car.needs_service()) #battery does not need service cause its less than 4 years
        #engine does not need service because mileage difference is less than 60000
        #tires do need service cause sum is  greater than 3
    
    def test_rorschach_does_not_need_service(self):
        car = CarFactory.create_rorschach(date(2023, 8, 1), date(2022, 8, 1), 80000, 75000, [0.1, 0.2, 0.3, 0.5])
        self.assertFalse(car.needs_service()) #battery does not need service cause its less than 4 years
        #engine does not need service because mileage difference is less than 60000
        #tires do not need service cause sum is not greater than 3
    
    def test_thovex_battery_needs_service(self):
        car = CarFactory.create_thovex(date(2023, 8, 1), date(2016, 8, 1), 80000, 60000, [0.1, 0.8, 0.3, 0.5])
        self.assertTrue(car.needs_service()) #battery needs service cause its more than 4 years
        #engine does not need service because mileage difference is less than 30000
        #tires do not need service cause none are greater than 0.9
    
    def test_thovex_engine_needs_service(self):
        car = CarFactory.create_thovex(date(2023, 8, 1), date(2022, 8, 1), 50000, 10000, [0.1, 0.8, 0.3, 0.5])
        self.assertTrue(car.needs_service()) #battery does not need service cause its less than 4 years
        #engine needs service cause mileage difference is greater than 30000
        #tires do not need service cause none are greater than 0.9
    
    def test_thovex_tires_needs_service(self):
        car = CarFactory.create_thovex(date(2023, 8, 1), date(2022, 8, 1), 50000, 10000, [0.1, 0.9, 0.3, 0.5])
        self.assertTrue(car.needs_service()) #battery does not need service cause its less than 4 years
        #engine needs service cause mileage difference is greater than 30000
        #tires do need service cause one is greater than 0.9

    def test_thovex_does_not_need_service(self):
        car = CarFactory.create_thovex(date(2023, 8, 1), date(2022, 8, 1), 30000, 25000, [0.1, 0.8, 0.3, 0.5])
        self.assertFalse(car.needs_service())  #battery does not need service cause its less than 4 years
        ##engine does not need service because mileage difference is less than 30000
        #tires do not need service cause none are greater than 0.9
