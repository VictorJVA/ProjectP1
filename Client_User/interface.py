from abc import ABC, abstractmethod

class Entity(ABC):
    @abstractmethod
    def display_info(self):
        pass