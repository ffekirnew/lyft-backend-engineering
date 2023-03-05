import unittest

from engines.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        current_mileage = 70_000
        last_service_mileage = 0

        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby_engine.needs_service())

    def test_engine_does_not_need_service(self):
        current_mileage = 0
        last_service_mileage = 0

        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(not willoughby_engine.needs_service())


if __name__ == "__main__":
    unittest.main()
