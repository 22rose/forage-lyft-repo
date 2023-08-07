import unittest
from datetime import date
from parts.Battery.nubbin_battery import NubbinBattery
from parts.Battery.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date(2018, 1, 1)
        current_date = date(2022, 2, 1)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date(2020, 1, 1)
        current_date = date(2022, 2, 1)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date(2018, 1, 1)
        current_date = date(2022, 2, 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date(2020, 1, 1)
        current_date = date(2022, 2, 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
