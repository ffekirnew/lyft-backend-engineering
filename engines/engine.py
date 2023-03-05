from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        """
        Abstract class to be implemented by users, shows if an engines needs to be serviced.
        :return: boolean
        """
        pass
