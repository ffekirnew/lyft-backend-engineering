from tires.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, wear_level):
        self.__wear_level = wear_level

    def needs_service(self):
        # Octoprime tires should be serviced when the sum of all values in the tire wear array is greater than or equal to 3.
        return sum(self.__wear_level) >= 3
