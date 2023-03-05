import unittest

from tires.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_needs_service(self):
        wear_level = [0.9, 0.8, 0.3, 1]

        octoprime_tire = OctoprimeTire(wear_level)
        self.assertTrue(octoprime_tire.needs_service())

    def test_tire_does_not_need_service(self):
        wear_level = [0.1, 0.2, 0.3, 0.4]

        octoprime_tire = OctoprimeTire(wear_level)
        self.assertTrue(not octoprime_tire.needs_service())


if __name__ == "__main__":
    unittest.main()
