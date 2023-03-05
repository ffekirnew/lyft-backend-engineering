from abc import ABC, abstractmethod


class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        """
        Abstract method to be implemented by users, shows if a batteries needs to be serviced.
        :return:
        """
        pass