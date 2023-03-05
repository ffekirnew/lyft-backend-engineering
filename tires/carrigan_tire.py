from tires.tire import Tire


class CarriganTire(Tire):
    def __init__(self, wear_level):
        self.__wear_level = wear_level

    def needs_service(self):
        # Carrigan tires should be serviced when one or more of the values in the tire wear array is greater than or equal to 0.9
        return any(wear >= 0.9 for wear in self.__wear_level)
