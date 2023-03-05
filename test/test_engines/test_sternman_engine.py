import unittest

from engines.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        warning_light_is_on = True

        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman_engine.needs_service())

    def test_engine_does_not_need_service(self):
        warning_light_is_on = False

        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(not sternman_engine.needs_service())


if __name__ == "__main__":
    unittest.main()
