from abc import ABC, abstractmethod
"""Base class for battery"""
"""Adding a new battery is as simple as creating a new
class which implements this given interface."""


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass
