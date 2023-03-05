from abc import ABC, abstractmethod


class Servicable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        """
        Abstract class to be implemented by users, shows if a servicable needs to be serviced.
        :return: boolean
        """
        pass
