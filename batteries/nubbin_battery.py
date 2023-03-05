from batteries.battery import Battery
from utils import add_years


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self) -> bool:
        date_for_service = add_years(self.__last_service_date, 4)
        return self.__current_date > date_for_service