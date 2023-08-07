import unittest
from parts.Tire.carrigan_tire import CarriganTire
from parts.Tire.octoprime_tire import OctoprimeTire


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.1, 0.9, 0.3, 0.5]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.8, 0.3, 0.5]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9, 0.9, 0.9, 0.9]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.2, 0.3, 0.5]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())

