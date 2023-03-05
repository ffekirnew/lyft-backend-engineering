from batteries.battery import Battery
from engines.engine import Engine
from servicable import Servicable
from tires.tire import Tire


class Car(Servicable):
    """
    Model a real life car in lyft's car fleet.
    """
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.__engine = engine
        self.__battery = battery
        self.__tire = tire

    def needs_service(self) -> bool:
        """
        Signify if a car needs service.
        :return: boolean ( true / false ) showing if a car needs a service.
        """
        return self.__engine.needs_service() and self.__battery.needs_service() and self.__tire.needs_service()
