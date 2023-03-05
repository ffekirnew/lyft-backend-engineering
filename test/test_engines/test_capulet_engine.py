import unittest

from engines.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        current_mileage = 40_000
        last_service_mileage = 0

        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet_engine.needs_service())

    def test_engine_does_not_need_service(self):
        current_mileage = 0
        last_service_mileage = 0

        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(not capulet_engine.needs_service())


if __name__ == "__main__":
    unittest.main()
