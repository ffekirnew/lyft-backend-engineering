from car import Car

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        calliope_car = Car(capulet_engine, spindler_battery)

        return calliope_car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        glissade_car = Car(willoughby_engine, spindler_battery)

        return glissade_car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        palindrome_car = Car(sternman_engine, spindler_battery)

        return palindrome_car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        rorschach_car = Car(willoughby_engine, nubbin_battery)

        return rorschach_car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        thovex_car = Car(capulet_engine, nubbin_battery)

        return thovex_car
