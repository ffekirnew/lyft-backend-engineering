from engines.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.__warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        if self.__warning_light_is_on:
            return True
        else:
            return False
