import unittest
from datetime import datetime

from batteries.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        nubbin_battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(nubbin_battery.needs_service())

    def test_battery_does_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        nubbin_battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(not nubbin_battery.needs_service())


if __name__ == "__main__":
    unittest.main()
