import unittest

from tires.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_needs_service(self):
        wear_level = [0.1, 0.2, 0.3, 1]

        carrigan_tire = CarriganTire(wear_level)
        self.assertTrue(carrigan_tire.needs_service())

    def test_tire_does_not_need_service(self):
        wear_level = [0.1, 0.2, 0.3, 0.4]

        carrigan_tire = CarriganTire(wear_level)
        self.assertTrue(not carrigan_tire.needs_service())


if __name__ == "__main__":
    unittest.main()
