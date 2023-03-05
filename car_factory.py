from car import Car

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_level):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        carrigan_tire = CarriganTire(tire_wear_level)

        calliope_car = Car(capulet_engine, spindler_battery, carrigan_tire)

        return calliope_car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_level):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        carrigan_tire = CarriganTire(tire_wear_level)

        glissade_car = Car(willoughby_engine, spindler_battery, carrigan_tire)

        return glissade_car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear_level):
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        octoprime_tire = OctoprimeTire(tire_wear_level)

        palindrome_car = Car(sternman_engine, spindler_battery, octoprime_tire)

        return palindrome_car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_level):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        octoprime_tire = OctoprimeTire(tire_wear_level)

        rorschach_car = Car(willoughby_engine, nubbin_battery, octoprime_tire)

        return rorschach_car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_level):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        octoprime_tire = OctoprimeTire(tire_wear_level)

        thovex_car = Car(capulet_engine, nubbin_battery, octoprime_tire)

        return thovex_car
