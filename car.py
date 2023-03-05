from batteries.battery import Battery
from engines.engine import Engine
from servicable import Servicable


class Car(Servicable):
    """
    Model a real life car in lyft's car fleet.
    """
    def __init__(self, engine: Engine, battery: Battery):
        self.__engine = engine
        self.__battery = battery

    def needs_service(self) -> bool:
        """
        Signify if a car needs service.
        :return: boolean ( true / false ) showing if a car needs a service.
        """
        return self.__engine.needs_service() and self.__battery.needs_service()
