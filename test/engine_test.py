import unittest
from parts.Engine.capulet_engine import CapuletEngine
from parts.Engine.sternman_engine import SternmanEngine
from parts.Engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = CapuletEngine(10000, 50000)
        self.assertTrue(engine.needs_service())
    
    def test_needs_service_false(self):
        engine = CapuletEngine(10000, 20000)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = WilloughbyEngine(40000, 110000)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = WilloughbyEngine(40000, 60000)
        self.assertFalse(engine.needs_service())

